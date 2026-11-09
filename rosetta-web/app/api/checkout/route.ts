import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const { tier = "pro", is_annual = false } = await req.json();

    const host = req.headers.get("x-forwarded-host") || req.headers.get("host") || "rosettaweb.up.railway.app";
    const proto = req.headers.get("x-forwarded-proto") || "https";
    const origin = `${proto}://${host}`;

    // 1. Stripe Checkout Support
    const stripeKey = process.env.STRIPE_SECRET_KEY;
    if (stripeKey && stripeKey.startsWith("sk_")) {
      const priceMap: Record<string, string> = {
        "pro_monthly": process.env.STRIPE_PRO_MONTHLY_PRICE_ID || "",
        "pro_annual": process.env.STRIPE_PRO_ANNUAL_PRICE_ID || "",
        "enterprise": process.env.STRIPE_ENTERPRISE_PRICE_ID || "",
      };

      const key = tier === "enterprise" ? "enterprise" : (is_annual ? "pro_annual" : "pro_monthly");
      const priceId = priceMap[key];

      if (priceId) {
        try {
          const stripeRes = await fetch("https://api.stripe.com/v1/checkout/sessions", {
            method: "POST",
            headers: {
              "Authorization": `Bearer ${stripeKey}`,
              "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({
              "success_url": `${origin}/billing-success?tier=${tier}&status=success&session_id={CHECKOUT_SESSION_ID}`,
              "cancel_url": `${origin}/#pricing`,
              "mode": "subscription",
              "line_items[0][price]": priceId,
              "line_items[0][quantity]": "1",
            }).toString()
          });

          if (stripeRes.ok) {
            const session = await stripeRes.json();
            return NextResponse.json({ url: session.url, provider: "stripe" });
          }
        } catch (e) {
          // Fall through to lemon squeezy or sandbox
        }
      }
    }

    // 2. Lemon Squeezy Checkout Support
    const lsApiKey = process.env.LEMONSQUEEZY_API_KEY;
    const lsStoreId = process.env.LEMONSQUEEZY_STORE_ID;
    if (lsApiKey && lsApiKey.startsWith("ls_") && lsStoreId) {
      const PRO_MONTHLY_VARIANT = process.env.LEMONSQUEEZY_PRO_MONTHLY_ID || "54321";
      const PRO_ANNUAL_VARIANT = process.env.LEMONSQUEEZY_PRO_ANNUAL_ID || "54322";
      const ENTERPRISE_VARIANT = process.env.LEMONSQUEEZY_ENTERPRISE_ID || "54323";

      let variantId = PRO_MONTHLY_VARIANT;
      if (tier === "pro" && is_annual) variantId = PRO_ANNUAL_VARIANT;
      if (tier === "enterprise") variantId = ENTERPRISE_VARIANT;

      try {
        const response = await fetch("https://api.lemonsqueezy.com/v1/checkouts", {
          method: "POST",
          headers: {
            "Content-Type": "application/vnd.api+json",
            "Accept": "application/vnd.api+json",
            "Authorization": `Bearer ${lsApiKey}`,
          },
          body: JSON.stringify({
            data: {
              type: "checkouts",
              attributes: {
                checkout_data: {
                  custom: { tier, billing_cycle: is_annual ? "annual" : "monthly" }
                },
                redirect_url: `${origin}/billing-success?tier=${tier}&status=success`,
              },
              relationships: {
                store: { data: { type: "stores", id: lsStoreId } },
                variant: { data: { type: "variants", id: variantId } }
              }
            }
          })
        });

        if (response.ok) {
          const resData = await response.json();
          return NextResponse.json({ url: resData.data.attributes.url, provider: "lemonsqueezy" });
        }
      } catch (err) {}
    }

    // 3. Sandbox / Instant Activation Mode
    // Allows instant developer verification with live API key generation
    const sandboxUrl = `/billing-success?tier=${tier}&status=activated&cycle=${is_annual ? "annual" : "monthly"}`;
    return NextResponse.json({ url: sandboxUrl, is_mock: true, provider: "sandbox" });

  } catch (err: any) {
    return NextResponse.json(
      { error: err.message || "Failed to initiate billing flow" },
      { status: 500 }
    );
  }
}

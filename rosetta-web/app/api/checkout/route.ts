import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const { tier, is_annual } = await req.json();

    const apiKey = process.env.LEMONSQUEEZY_API_KEY;
    const storeId = process.env.LEMONSQUEEZY_STORE_ID || "12345"; // placeholder Store ID
    
    // Check if we have a real production Lemon Squeezy API key
    const isRealConfig = apiKey && apiKey !== "your-lemon-squeezy-key" && apiKey.startsWith("ls_");

    if (isRealConfig) {
      // Standard variant mapping
      // In production, these should match your Lemon Squeezy dashboard Variant IDs
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
            "Authorization": `Bearer ${apiKey}`,
          },
          body: JSON.stringify({
            data: {
              type: "checkouts",
              attributes: {
                checkout_data: {
                  custom: {
                    tier,
                    billing_cycle: is_annual ? "annual" : "monthly"
                  }
                },
                redirect_url: `${req.nextUrl.origin}/billing-success?tier=${tier}&status=success`,
              },
              relationships: {
                store: {
                  data: {
                    type: "stores",
                    id: storeId
                  }
                },
                variant: {
                  data: {
                    type: "variants",
                    id: variantId
                  }
                }
              }
            }
          })
        });

        if (response.ok) {
          const resData = await response.json();
          const checkoutUrl = resData.data.attributes.url;
          return NextResponse.json({ url: checkoutUrl, is_mock: false });
        }
      } catch (err) {
        // Fallback below if API request fails
      }
    }

    // Sandbox / Local Fallback Mode
    const sandboxUrl = `/billing-success?tier=${tier}&status=activated&cycle=${is_annual ? "annual" : "monthly"}`;
    return NextResponse.json({ url: sandboxUrl, is_mock: true });

  } catch (err: any) {
    return NextResponse.json(
      { error: err.message || "Failed to initiate billing flow" },
      { status: 500 }
    );
  }
}

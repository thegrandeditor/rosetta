import { NextRequest, NextResponse } from "next/server";
import crypto from "crypto";

export async function POST(req: NextRequest) {
  try {
    const rawBody = await req.text();
    const signature = req.headers.get("x-signature") || "";
    const secret = process.env.LEMONSQUEEZY_WEBHOOK_SECRET;

    // Verify signature if secret is provided
    if (secret) {
      const hmac = crypto.createHmac("sha256", secret);
      const digest = Buffer.from(hmac.update(rawBody).digest("hex"), "utf8");
      const signatureBuffer = Buffer.from(signature, "utf8");

      if (digest.length !== signatureBuffer.length || !crypto.timingSafeEqual(digest, signatureBuffer)) {
        return NextResponse.json({ error: "Invalid signature" }, { status: 401 });
      }
    }

    const payload = JSON.parse(rawBody);
    const eventName = payload.meta?.event_name;
    const customData = payload.meta?.custom_data || {};
    const attributes = payload.data?.attributes || {};

    console.log(`[LemonSqueezy Webhook] Received event: ${eventName}`, {
      user_email: attributes.user_email,
      customer_id: attributes.customer_id,
      tier: customData.tier,
    });

    // Handle subscription lifecycle
    switch (eventName) {
      case "subscription_created":
      case "order_created": {
        const userEmail = attributes.user_email;
        const tier = customData.tier || "pro";
        // Generate a deterministic license API key
        const apiKey = `RSTA-${tier.toUpperCase()}-${crypto.randomBytes(8).toString("hex")}`;

        console.log(`[License Provisioned] Plan: ${tier} | User: ${userEmail} | Key: ${apiKey}`);
        // In a production database, you would save:
        // await db.licenses.create({ email: userEmail, apiKey, tier, status: "active" });
        break;
      }

      case "subscription_cancelled":
      case "subscription_expired": {
        console.log(`[License Revoked] User: ${attributes.user_email}`);
        // await db.licenses.update({ email: attributes.user_email, status: "cancelled" });
        break;
      }

      default:
        console.log(`[LemonSqueezy] Unhandled event: ${eventName}`);
    }

    return NextResponse.json({ received: true });
  } catch (err: any) {
    console.error("[LemonSqueezy Webhook Error]:", err);
    return NextResponse.json({ error: err.message || "Webhook processing failed" }, { status: 500 });
  }
}

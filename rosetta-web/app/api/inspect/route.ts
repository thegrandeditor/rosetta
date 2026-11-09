import { NextRequest, NextResponse } from "next/server";

export async function GET(req: NextRequest) {
  const accept = req.headers.get("accept") || "";
  if (accept.includes("text/html")) {
    const host = req.headers.get("x-forwarded-host") || req.headers.get("host") || "rosettaweb.up.railway.app";
    const proto = req.headers.get("x-forwarded-proto") || "https";
    return NextResponse.redirect(`${proto}://${host}/transpile`);
  }
  return NextResponse.json({
    status: "online",
    service: "ROSETTA Inspect API",
    method: "POST",
    usage: { source: "string", from_lang: "string", to_lang: "string" },
    ui_workbench: "/transpile"
  });
}

export async function POST(req: NextRequest) {
  try {
    const { source, from_lang, to_lang } = await req.json();
    const apiBase = (process.env.ROSETTA_API_URL || process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8008").replace(/\/$/, "");

    const response = await fetch(`${apiBase}/api/inspect`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ source, from_lang, to_lang }),
      signal: AbortSignal.timeout(4000),
    });

    if (response.ok) {
      const data = await response.json();
      return NextResponse.json(data);
    }

    return NextResponse.json(
      { error: "Failed to inspect AST via Rosetta engine" },
      { status: response.status }
    );
  } catch (err: any) {
    return NextResponse.json(
      { error: err.message || "Failed to inspect AST" },
      { status: 500 }
    );
  }
}

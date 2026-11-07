import { NextRequest, NextResponse } from "next/server";

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

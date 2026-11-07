import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const apiBase = (process.env.ROSETTA_API_URL || process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8008").replace(/\/$/, "");

    const response = await fetch(`${apiBase}/api/learn`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
      signal: AbortSignal.timeout(8000),
    });

    if (response.ok) {
      const data = await response.json();
      return NextResponse.json(data);
    }
    const errText = await response.text();
    return NextResponse.json({ error: errText }, { status: response.status });
  } catch (err: any) {
    return NextResponse.json(
      { error: err.message || "Failed to reach Rosetta Auto-Learn engine (ensure ROSETTA_API_URL is configured)" },
      { status: 500 }
    );
  }
}

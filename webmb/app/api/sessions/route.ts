import crypto from "crypto"
import { NextRequest } from "next/server"
export async function POST(request: NextRequest) {
    const sessionID = crypto.randomBytes(16).toString("hex")
    return Response.json({sessionID})
}

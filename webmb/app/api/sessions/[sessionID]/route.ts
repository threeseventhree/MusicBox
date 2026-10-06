import { getSession } from "@/app/lib/sessionStore"
import { NextRequest } from "next/server"

export async function GET(request: NextRequest,{params}: {params: Promise<{ sessionID: string }>}) {
    const { sessionID } = await params
    const session = await getSession(sessionID)
    return Response.json({connected: session?.connected ?? false})
}

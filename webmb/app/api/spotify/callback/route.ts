import { getSession, setSessionConnected } from "@/app/lib/sessionStore"
import { redirect } from "next/navigation"
import { NextRequest } from "next/server"

export async function GET(request: NextRequest) {
    const sessionID = request.nextUrl.searchParams.get("sessionID")
    const state = request.nextUrl.searchParams.get("state")
    if (!sessionID || !state) {return new Response("Missing parameters", { status: 400 })}

    const session = await getSession(sessionID)
    if (!session) {return new Response("Session not found", { status: 404 })}
    if (session.state !== state) {return new Response("Invalid state", { status: 400 })}
    await setSessionConnected(sessionID)
    
    redirect(`/connect/${sessionID}/success`)
}

import { redirect } from "next/navigation"
import { NextRequest } from "next/server"
//upon clicking the button we will travel to this api route which will send us to the spotify auth page
export async function GET(request: NextRequest) {
    const sessionID = request.nextUrl.searchParams.get("sessionID")
    const state = request.nextUrl.searchParams.get("state")
    if (!sessionID || !state) {return new Response("Missing parameters", { status: 400 })}
    redirect(`/api/spotify/callback?sessionID=${sessionID}&state=${state}`)
}

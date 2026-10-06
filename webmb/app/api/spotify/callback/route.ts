import {
    getSessionByState,
    setSessionConnected
} from "@/app/lib/sessionStore"

import { NextRequest } from "next/server"
import { redirect } from "next/navigation"

export async function GET(request: NextRequest) {
    const code = request.nextUrl.searchParams.get("code")
    const state = request.nextUrl.searchParams.get("state")
    if (!code || !state) {return new Response("Missing parameters", { status: 400 })}

    const session = await getSessionByState(state)
    if (!session) {return new Response("Session not found", { status: 404 })}
    if (session.state !== state) {return new Response("Invalid state",{ status: 400 })}

    const clientID = process.env.SPOTIFY_CLIENT_ID
    const clientSecret = process.env.SPOTIFY_CLIENT_SECRET
    const redirectURI = process.env.SPOTIFY_REDIRECT_URI
    if (!clientID || !clientSecret || !redirectURI) {throw new Error("Spotify environment variables are missing")}

    const tokenResponse = await fetch(
        "https://accounts.spotify.com/api/token",
        {
            method: "POST",
            headers: {
                "Content-Type":
                    "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                grant_type: "authorization_code",
                code: code,
                redirect_uri: redirectURI,
                client_id: clientID,
                client_secret: clientSecret
            })
        }
    )
    if (!tokenResponse.ok) {
        const error = await tokenResponse.text()
        console.error("Spotify token exchange failed:", error)
        return new Response("Spotify authorization failed", { status: 400 })
    }

    const tokens = await tokenResponse.json()
    console.log(tokens)
    await setSessionConnected(session.sessionID, tokens.access_token, tokens.refresh_token, tokens.expires_in)
    redirect(`/connect/${session.sessionID}/success`)
}

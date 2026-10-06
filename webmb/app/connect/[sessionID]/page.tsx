import crypto from "crypto"
import { createSession } from "@/app/lib/sessionStore"
import { redirect } from "next/navigation"

export default async function ConnectPage({params}: {params: Promise<{ sessionID: string }>}) {
    const { sessionID } = await params
    const state = crypto.randomBytes(16).toString("hex")
    await createSession(sessionID, state)
    const clientID = process.env.SPOTIFY_CLIENT_ID
    const redirectURI = process.env.SPOTIFY_REDIRECT_URI
    if (!clientID || !redirectURI) {throw new Error("Spotify environment variables are missing")}
    const spotifyParams = new URLSearchParams({
        client_id: clientID,
        response_type: "code",
        redirect_uri: redirectURI,
        state: state,
        scope: "user-read-currently-playing"
    })

    redirect(
        `https://accounts.spotify.com/authorize?${spotifyParams.toString()}`
    )
}

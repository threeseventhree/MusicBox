import { getValidAccessToken } from "@/app/lib/sessionStore"
import { NextRequest } from "next/server"

export async function GET(request: NextRequest,{ params }: {params: Promise<{ sessionID: string }>}) {
    const { sessionID } = await params
    const accessToken = await getValidAccessToken(sessionID)
    if (!accessToken) {return Response.json({error: "Spotify session unavailable" }, { status: 401 })}
    const spotifyResponse = await fetch(
        "https://api.spotify.com/v1/me/player/currently-playing",
        {
            headers: {
                Authorization: `Bearer ${accessToken}`
            }
        }
    )
    if (spotifyResponse.status === 204) {return Response.json({playing: false})}
    if (!spotifyResponse.ok) {
        const error = await spotifyResponse.text()
        console.error("Spotify currently-playing failed:", error)
        return Response.json({error: "Spotify API request failed"}, { status: spotifyResponse.status })
    }
    const data = await spotifyResponse.json()
    const track = data.item
    return Response.json({
        playing: data.is_playing,
        progressMs: data.progress_ms,
        durationMs: track.duration_ms,
        title: track.name,
        artist: track.artists[0]?.name,
        album: track.album.name,
        artworkURL: track.album.images[0]?.url,
        songUrl: track.external_urls.spotify
    })
}

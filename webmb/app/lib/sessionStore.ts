import { Redis } from "@upstash/redis"

export type Session = {
    sessionID: string
    state: string
    connected: boolean
    accessToken?: string
    refreshToken?: string
    expiresAt?: number
}

const redis = Redis.fromEnv()
function getKey(sessionID: string) {
    return `session:${sessionID}`
}

export async function createSession(sessionID: string, state: string) {
    const session: Session = {
        sessionID,
        state,
        connected: false
    }
    await redis.set(
        `session:${sessionID}`, session,
        {
            ex: 900
        }
    )
    await redis.set(
        `state:${state}`, sessionID,
        {
            ex: 900
        }
    )
}

export async function getSession(sessionID: string): Promise<Session | null> {
    return await redis.get<Session>(
        getKey(sessionID)
    )
}

export async function setSessionConnected(sessionID: string, accessToken: string, refreshToken: string, expiresIn: number) {
    const session = await getSession(sessionID)
    if (!session) {return false}
    session.connected = true
    session.accessToken = accessToken
    session.refreshToken = refreshToken
    session.expiresAt = Date.now() + expiresIn * 1000
    await redis.set(
        getKey(sessionID),
        session,
    )
    return true
}

export async function getSessionByState(state: string): Promise<Session | null> {
    const sessionID = await redis.get<string>(`state:${state}`)
    if (!sessionID) {return null}
    return await getSession(sessionID)
}

export async function getValidAccessToken(sessionID: string): Promise<string | null> {
    const session = await getSession(sessionID)
    if (!session || !session.connected) {return null}
    if (!session.accessToken || !session.refreshToken) {return null}
    const isValid = session.expiresAt !== undefined && Date.now() < session.expiresAt - 60_000
    if (isValid) {return session.accessToken}
    console.log("Spotify access token expired, refreshing...")
    const clientID = process.env.SPOTIFY_CLIENT_ID
    const clientSecret = process.env.SPOTIFY_CLIENT_SECRET

    if (!clientID || !clientSecret) {throw new Error("Spotify environment variables are missing")}
    const tokenResponse = await fetch(
        "https://accounts.spotify.com/api/token",
        {
            method: "POST",
            headers: {
                "Content-Type":
                    "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                grant_type: "refresh_token",
                refresh_token: session.refreshToken,
                client_id: clientID,
                client_secret: clientSecret
            })
        }
    )
    if (!tokenResponse.ok) {
        const error = await tokenResponse.text()
        console.error("Spotify token refresh failed:", error)
        return null
    }
    const tokens = await tokenResponse.json()
    session.accessToken = tokens.access_token
    if (tokens.refresh_token) {session.refreshToken = tokens.refresh_token}
    session.expiresAt = Date.now() + tokens.expires_in * 1000
    await redis.set(
        getKey(sessionID),
        session
    )
    return tokens.access_token
}

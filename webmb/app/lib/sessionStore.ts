import { Redis } from "@upstash/redis"

export type Session = {
    state: string
    connected: boolean
}

const redis = Redis.fromEnv()

function getKey(sessionID: string) {
    return `session:${sessionID}`
}

export async function createSession(sessionID: string,state: string) {
    const session: Session = {state, connected: false}
    await redis.set(
        getKey(sessionID),
        session,
        {
            ex: 900 //expires in 900sec or 15min
        }
    )
}

export async function getSession(sessionID: string): Promise<Session | null> {
    return await redis.get<Session>(
        getKey(sessionID)
    )
}

export async function setSessionConnected(sessionID: string) {
    const session = await getSession(sessionID)
    if (!session) {return false}
    session.connected = true
    await redis.set(
        getKey(sessionID),
        session,
        {
            ex: 900
        }
    )
    return true
}

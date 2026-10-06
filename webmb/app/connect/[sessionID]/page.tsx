import { createSession } from "@/app/lib/sessionStore"
import crypto from "crypto"
import { redirect } from "next/navigation"
//get the session id and assign it to a session, generate a state which will be kept and passed throughout our browsing experience.
export default async function ConnectPage({params}: {params: Promise<{sessionID: string}>}) {
    const { sessionID } = await params
    const state = crypto.randomBytes(16).toString("hex")
    await createSession(sessionID, state)
    redirect(`/api/fake-spotify?sessionID=${sessionID}&state=${state}`)
}

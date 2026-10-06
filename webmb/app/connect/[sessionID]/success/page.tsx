export default async function SuccessPage({params}: {params: Promise<{ sessionID: string }>}) {
    const { sessionID } = await params
    return (
        <main>
            <h1>MusicBox</h1>
            <p>Spotify connected successfully.</p>
            <p>Session: {sessionID}</p>
        </main>
    )
}

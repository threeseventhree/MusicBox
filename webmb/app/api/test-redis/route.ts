import { Redis } from "@upstash/redis"

const redis = Redis.fromEnv()
//there is a key named "musicbox-test" created automatically and we set the value of that key to hello, then we get and display it!
export async function GET() {
    await redis.set("musicbox-test", "hello")

    const value = await redis.get("musicbox-test")

    return Response.json({
        value
    })
}

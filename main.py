from src.shazam.recognizer import ShazamRecognizer
import asyncio

async def main():
    shazam = ShazamRecognizer()
    data = await shazam.getTrackData("audio/IN2THAT.mp3")
    track = await shazam.convertDataToTrack(data)
    print(track)
    

if __name__ == "__main__":
    asyncio.run(main())
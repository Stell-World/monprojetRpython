import asyncio
import base64
from pathlib import Path

from dotenv import load_dotenv
from rodiumai import RodiumAI


load_dotenv()

CHAT_MODEL = "openai/gpt-4o"
IMAGE_MODEL = "openai/gpt-image-1"
VIDEO_MODEL = "google/veo-3.1"


client = RodiumAI(
    default_model=CHAT_MODEL,
    timeout=30.0,
    stream_timeout=150.0
)


async def chat():
    while True:
        print("\n--- ETAPE 1 : CHAT ---")

        prompt = input("Votre question : ")

        try:
            response = await client.chat(
                prompt,
                model=CHAT_MODEL
            )

            print("\nRéponse :")
            print(response.choices[0].message.content)

            if hasattr(response, "cost_rodi"):
                print(f"\nCoût : {response.cost_rodi} RODI")

        except Exception as error:
            print("\nErreur :")
            print(error)

        choix = input(
            "\n[r] Répéter | [s] Suivant : "
        ).lower()

        if choix == "s":
            return


async def image():
    while True:
        print("\n--- ETAPE 2 : IMAGE ---")

        prompt = input("Description de l'image : ")

        try:
            response = await client.images(
                model=IMAGE_MODEL,
                prompt=prompt,
                n=1,
                size="1024x1024",
                quality="medium"
            )

            image_data = response.data[0].b64_json

            image_bytes = base64.b64decode(image_data)

            with open("image.png", "wb") as file:
                file.write(image_bytes)

            print("\nImage créée avec succès.")
            print("Fichier : image.png")

            if hasattr(response, "cost_rodi"):
                print(f"Coût : {response.cost_rodi} RODI")

        except Exception as error:
            print("\nErreur :")
            print(error)

        choix = input(
            "\n[b] Retour | [r] Répéter | [s] Suivant : "
        ).lower()

        if choix == "b":
            return "back"

        if choix == "s":
            return "next"


async def video():
    while True:
        print("\n--- ETAPE 3 : VIDEO ---")

        prompt = input("Description de la vidéo : ")

        try:
            response = await client.videos(
                model=VIDEO_MODEL,
                prompt=prompt,
                duration_seconds=4
            )

            video_data = response.data[0].b64_json

            video_bytes = base64.b64decode(video_data)

            with open("video.mp4", "wb") as file:
                file.write(video_bytes)

            print("\nVidéo créée avec succès.")
            print("Fichier : video.mp4")

            if hasattr(response, "cost_rodi"):
                print(f"Coût : {response.cost_rodi} RODI")

        except Exception as error:
            print("\nErreur :")
            print(error)

        choix = input(
            "\n[b] Retour | [r] Répéter | [q] Quitter : "
        ).lower()

        if choix == "b":
            return "back"

        if choix == "q":
            return "quit"


async def main():
    etape = 1

    while True:

        if etape == 1:
            await chat()
            etape = 2

        elif etape == 2:
            resultat = await image()

            if resultat == "back":
                etape = 1

            elif resultat == "next":
                etape = 3

        elif etape == 3:
            resultat = await video()

            if resultat == "back":
                etape = 2

            elif resultat == "quit":
                print("\nProgramme terminé.")
                break


if __name__ == "__main__":
    asyncio.run(main())
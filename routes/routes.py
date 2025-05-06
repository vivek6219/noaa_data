from fastapi import APIRouter
import httpx

base_url = "https://api.weather.gov/"
router = APIRouter()

@router.get("/glossary")
async def get_glossary():
    glossary_url = base_url+"/glossary"
    print(glossary_url)
    async with httpx.AsyncClient() as client:
        response = await client.get(url=glossary_url)
        print(response)
        data = response.json()
    return data

@router.get("/zones")
async def get_zones():
    zones_url = base_url+"/zones"
    async with httpx.AsyncClient() as client:
        response = await client.get(url=zones_url)
        print(response)
        data = response.json()
    return data
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
from mangum import Mangum


app = FastAPI()

# declare origin/s
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# @app.get("/test/{zone}")
# def read_forcast(zone: str, q: str):
#     return [{"zone": zone, "q": q}]

@app.get("/test/avalanchedanger")
def read__test__avalanchedanger():
    return {
      "level": "Considerable",
      "description":
        "Dangerous avalanche conditions. Careful snowpack evaluation, cautious route-finding and conservative decision-making essential.",
    }
@app.get("/test/skirunlist")
def read__test__skirunlist():
    return [
        { "name": "Cornice Run", "difficulty": "Expert", "available": True, "aspect": "North", "max_slope_angle": 50, "average_slope_angle": 38, "route_up": "Hike from Chair 7" },
        { "name": "Hellroaring Pk", "difficulty": "Advanced", "available": True, "aspect": "West", "max_slope_angle": 45, "average_slope_angle": 35, "route_up": "Skin track from base" },
        { "name": "Playground", "difficulty": "Intermediate", "available": True, "aspect": "South", "max_slope_angle": 40, "average_slope_angle": 30, "route_up": "Chair 7 drop-in" },
        { "name": "West Branch", "difficulty": "Expert", "available": False, "aspect": "Northwest", "max_slope_angle": 52, "average_slope_angle": 42, "route_up": "Hike access" },
        { "name": "North Branch", "difficulty": "Advanced", "available": True, "aspect": "East", "max_slope_angle": 47, "average_slope_angle": 37, "route_up": "Skin track from North Ridge" },
        { "name": "Star Trek", "difficulty": "Expert", "available": True, "aspect": "Southwest", "max_slope_angle": 55, "average_slope_angle": 45, "route_up": "Bootpack from Chair 8" },
        { "name": "Chair 7", "difficulty": "Easy", "available": True, "aspect": "North", "max_slope_angle": 25, "average_slope_angle": 15, "route_up": "Lift access" },
        { "name": "Chair 8", "difficulty": "Easy", "available": True, "aspect": "South", "max_slope_angle": 28, "average_slope_angle": 18, "route_up": "Lift access" },
        { "name": "Chair 11", "difficulty": "Easy", "available": True, "aspect": "West", "max_slope_angle": 30, "average_slope_angle": 20, "route_up": "Lift access" },
        { "name": "Lodi Pk", "difficulty": "Advanced", "available": False, "aspect": "Northeast", "max_slope_angle": 50, "average_slope_angle": 40, "route_up": "Bootpack access" },
        { "name": "Flower Pt", "difficulty": "Intermediate", "available": True, "aspect": "Southeast", "max_slope_angle": 35, "average_slope_angle": 25, "route_up": "Chair 11 drop-in" },
        { "name": "Banana", "difficulty": "Expert", "available": True, "aspect": "West", "max_slope_angle": 48, "average_slope_angle": 38, "route_up": "Hike from Ridge" },
        { "name": "7 Sisters", "difficulty": "Advanced", "available": True, "aspect": "East", "max_slope_angle": 42, "average_slope_angle": 32, "route_up": "Traverse from Chair 7" },
        { "name": "Bookshelf", "difficulty": "Intermediate", "available": True, "aspect": "North", "max_slope_angle": 30, "average_slope_angle": 22, "route_up": "Chair 11 drop-in" },
        { "name": "Fiberglass Hill", "difficulty": "Expert", "available": True, "aspect": "Southwest", "max_slope_angle": 55, "average_slope_angle": 45, "route_up": "Bootpack access" },
        { "name": "Canyon Creek", "difficulty": "Expert", "available": False, "aspect": "North", "max_slope_angle": 50, "average_slope_angle": 42, "route_up": "Skin access" },
        { "name": "Beaver Pond", "difficulty": "Intermediate", "available": True, "aspect": "East", "max_slope_angle": 32, "average_slope_angle": 24, "route_up": "Chair 11 drop-in" },
        { "name": "Ghoulie Pt", "difficulty": "Advanced", "available": True, "aspect": "West", "max_slope_angle": 45, "average_slope_angle": 35, "route_up": "Bootpack from Chair 7" },
        { "name": "Picked Egg", "difficulty": "Advanced", "available": False, "aspect": "South", "max_slope_angle": 48, "average_slope_angle": 38, "route_up": "Hike required" },
        { "name": "Baby’s Butt", "difficulty": "Expert", "available": True, "aspect": "Northwest", "max_slope_angle": 52, "average_slope_angle": 42, "route_up": "Hike access" },
        { "name": "Half Moon", "difficulty": "Intermediate", "available": True, "aspect": "Southeast", "max_slope_angle": 34, "average_slope_angle": 26, "route_up": "Chair 11 access" },
        { "name": "Michu Maker", "difficulty": "Advanced", "available": True, "aspect": "South", "max_slope_angle": 46, "average_slope_angle": 36, "route_up": "Traverse from Chair 8" },
        { "name": "Chicken Bones", "difficulty": "Expert", "available": True, "aspect": "West", "max_slope_angle": 50, "average_slope_angle": 40, "route_up": "Hike up ridge" },
        { "name": "Big Slide", "difficulty": "Advanced", "available": True, "aspect": "North", "max_slope_angle": 44, "average_slope_angle": 34, "route_up": "Traverse from Chair 7" },
        { "name": "Kona", "difficulty": "Intermediate", "available": True, "aspect": "Southeast", "max_slope_angle": 36, "average_slope_angle": 28, "route_up": "Chair 11 drop-in" },
        { "name": "Big Trees", "difficulty": "Advanced", "available": True, "aspect": "East", "max_slope_angle": 42, "average_slope_angle": 34, "route_up": "Skin access" },
        { "name": "Spruce Park", "difficulty": "Easy", "available": True, "aspect": "West", "max_slope_angle": 30, "average_slope_angle": 22, "route_up": "Lift access" },
        { "name": "Top of the World", "difficulty": "Expert", "available": False, "aspect": "North", "max_slope_angle": 55, "average_slope_angle": 45, "route_up": "Bootpack only" },
        { "name": "Land of Oz", "difficulty": "Intermediate", "available": True, "aspect": "Southwest", "max_slope_angle": 32, "average_slope_angle": 24, "route_up": "Chair 11 drop-in" },
        { "name": "Skookoleel", "difficulty": "Advanced", "available": True, "aspect": "East", "max_slope_angle": 100, "average_slope_angle": 30, "route_up": "Traverse from Chair 11" },
        { "name": "Auntie Em", "difficulty": "Advanced", "available": True, "aspect": "East", "max_slope_angle": 40, "average_slope_angle": 30, "route_up": "Traverse from Chair 7" },
        { "name": "Dorothy", "difficulty": "Intermediate", "available": True, "aspect": "South", "max_slope_angle": 30, "average_slope_angle": 22, "route_up": "Chair 11 access" }
    ]

# https://api.avalanche.org/v2/public/product?type=forecast&center_id=FAC&zone_id=1733
@app.get("/forcast/{zone}")
async def read__forcast(zone: str):
    url = "https://api.avalanche.org/v2/public/product?type=forecast&center_id=FAC&zone_id=1733"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    
    # Check for a successful response
    if response.status_code == 200:
        return response.json()  # Return the JSON data from the external API
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}
    
handler = Mangum(app)
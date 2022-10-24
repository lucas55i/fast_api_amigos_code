from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from modelo import PcConfig, UpdateConfig

app = FastAPI()

db: List[PcConfig] = [
    PcConfig(
        id=UUID("40ed577d-675f-45f5-85a7-eac9365730d8"),
        cpu="AMD Ryzen 5 4600g",
        ram="8gb 3200mhz",
        motherboard="A320",
        video_card="RTX 2060",
        hd_ssd="SSD m.2 256gb",
        source="600w"
    ),
    PcConfig(
        id=UUID("310154ca-bc30-4cb6-9168-72b55c7bad90"),
        cpu="AMD Ryzen 5 4600g",
        ram="8gb 3200mhz",
        motherboard="A320",
        video_card="RTX 2060",
        hd_ssd="SSD m.2 256gb",
        source="600w"
    ),
]


@app.get("/")
async def root():
    return "Olá mundo"


@app.get("/api/v1/pc")
async def get_pc():
    return db


@app.post("/api/v1/pc")
async def add_config(newConf: PcConfig):
    db.append(newConf)
    return {"Nova Configuração": newConf}


@app.delete("/api/v1/pc/{pc_id}")
async def delete_pc(pc_id: UUID):
    for pc in db:
        if pc.id == pc_id:
            db.remove(pc)
            return db
    raise HTTPException(
        status_code=404,
        detail=f"pc with id: {pc_id} does not exists"
    )


@app.put("/api/v1/pc/{pc_id}")
async def update_pc(pc_update: UpdateConfig, pc_id: UUID):
    for pc in db:
        if pc.id == pc_id:
            if pc_update.cpu is not None:
                pc.cpu = pc_update.cpu
            if pc_update.ram is not None:
                pc.ram = pc_update.ram
            if pc_update.motherboard is not None:
                pc.motherboard = pc_update.motherboard
            if pc_update.video_card is not None:
                pc.video_card = pc_update.video_card
            if pc_update.hd_ssd is not None:
                pc.hd_ssd = pc_update.hd_ssd
            if pc_update.source is not None:
                pc.source = pc_update.source
            return db
    raise HTTPException(
        status_code=404,
        detail=f"pc with id: {pc_id} does not exiists"
    )

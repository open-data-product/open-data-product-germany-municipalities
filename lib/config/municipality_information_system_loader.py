import os

import numpy as np
from pydantic import BaseModel, TypeAdapter
import pandas as pd


class MunicipalityInformationSystem(BaseModel):
    ags: str
    ars: str
    type: str
    sub_type: str
    municipality_name: str
    area_sqkm: float
    population_total: float
    population_male: float
    population_female: float
    population_per_sqkm: float
    zip_code: str
    center_lon: str
    center_lat: str
    degree_of_urbanization_key: str
    degree_of_urbanization_name: str


def load_municipality_information_systems(
    data_path, file_name="municipality-information-systems.csv"
) -> list[MunicipalityInformationSystem] | None:
    file_path = os.path.join(data_path, file_name)

    if os.path.exists(file_path):
        municipality_information_systems_dataframe = (
            pd.read_csv(file_path, dtype=str).replace({np.nan: None}).dropna()
        )

        municipality_information_systems = TypeAdapter(
            list[MunicipalityInformationSystem]
        ).validate_python(
            municipality_information_systems_dataframe.to_dict(orient="records")
        )
        return municipality_information_systems
    else:
        print(f"✗️ Config file {file_path} does not exist")

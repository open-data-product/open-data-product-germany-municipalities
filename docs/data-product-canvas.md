
# Data Product Canvas - Municipalities

## Metadata

* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-municipalities
* license: CC-BY 4.0
* updated: 2026-07-27

## Input Ports

### germany-municipalities-2026-06
name: Alle politisch selbständigen Gemeinden mit ausgewählten Merkmalen am 30.06.2026 (2. Quartal 2026)
* owner: Statistisches Bundesamt (Destatis)
* url: https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/Archiv/GVAuszugQ/AuszugGV2QAktuell.html
* license: Data Licence Germany – Attribution – Version 2.0
* updated: 2026-05-27

**Files**

* [AuszugGV2QAktuell.xlsx?__blob=publicationFile&v=13](https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/Archiv/GVAuszugQ/AuszugGV2QAktuell.xlsx?__blob=publicationFile&v=13)


### germany-municipalities-2026-03
name: Alle politisch selbständigen Gemeinden mit ausgewählten Merkmalen am 31.03.2026 (1. Quartal)
* owner: Statistisches Bundesamt (Destatis)
* url: https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/Archiv/GVAuszugQ/AuszugGV1QAktuell.html
* license: Data Licence Germany – Attribution – Version 2.0
* updated: 2026-02-25

**Files**

* [AuszugGV1QAktuell.xlsx?__blob=publicationFile&v=16](https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/Archiv/GVAuszugQ/AuszugGV1QAktuell.xlsx?__blob=publicationFile&v=16)


### germany-municipalities-geodata-2025-01
name: Verwaltungsgebiete 1:250 000 Stand 01.01. (VG250 01.01.)
* owner: Bundesamt für Kartographie und Geodäsie
* url: https://gdz.bkg.bund.de/index.php/default/verwaltungsgebiete-1-250-000-stand-01-01-vg250-01-01.html
* license: Data Licence Germany – Attribution – Version 2.0
* updated: 2025-01-01

**Files**

* [vg250_01-01.utm32s.shape.ebenen.zip](https://daten.gdz.bkg.bund.de/produkte/vg/vg250_ebenen_0101/aktuell/vg250_01-01.utm32s.shape.ebenen.zip)


## Transformation Steps

* [Data extractor](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/extract/data_extractor.py) extracts data from inout ports
* [Data copier](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/transform/data_copier.py) copies and renames extracted data
* [Data CSV converter](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/transform/data_csv_converter.py) converts Excel files to CSV format
* [Data aggregator](https://github.com/open-data-product/open-data-product-python-lib/blob/main/opendataproduct/transform/data_aggregator.py) aggregates data to be used as output ports

## Output Ports

### germany-municipalities-2026-03-csv
name: Germany Municipalities 2026 03 Csv
* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-municipalities/tree/main/data/03-gold/germany-municipalities-2026-03-csv
* license: CC-BY 4.0
* updated: 2026-07-27

**Files**

* [germany-municipalities-2026-03.csv](https://media.githubusercontent.com/media/open-data-product/open-data-product-municipalities/refs/heads/main/data/03-gold/germany-municipalities-2026-03-csv/germany-municipalities-2026-03.csv)


### germany-municipalities-2026-03-parquet
name: Germany Municipalities 2026 03 Parquet
* owner: Open Data Product
* url: https://github.com/open-data-product/open-data-product-municipalities/tree/main/data/03-gold/germany-municipalities-2026-03-parquet
* license: CC-BY 4.0
* updated: 2026-07-27

**Files**

* [germany-municipalities-2026-03.parquet](https://media.githubusercontent.com/media/open-data-product/open-data-product-municipalities/refs/heads/main/data/03-gold/germany-municipalities-2026-03-parquet/germany-municipalities-2026-03.parquet)


## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

source-aligned


---
This data product canvas uses the template of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).
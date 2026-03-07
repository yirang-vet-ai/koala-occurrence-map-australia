# Koala Occurrence Map Australia

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)]
[![Modular](https://img.shields.io/badge/design-modular-green)]
[![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)]

Interactive map project for visualizing koala occurrence records across Australia using Python, Pandas, and Folium.

Author: YIRANG JUNG  
License: Apache License 2.0

## Overview

This project loads koala occurrence data from a CSV file, cleans latitude and longitude values, samples records for performance, and renders an interactive HTML map with clustered koala emoji markers.

Each marker popup can display:
- Scientific name
- Observation start date
- Observation end date
- Locality details
- Project name
- Organisation acronym

## Repository Structure

```text
koala-occurrence-map-australia/
├─ data/
│  └─ koala_selected_columns.csv
├─ outputs/
│  └─ .gitkeep
├─ koala_map_generator.py
├─ koala1.ipynb
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md
```

## Features

- Loads koala observation data from CSV
- Converts coordinates to numeric format
- Drops invalid latitude and longitude rows
- Uses random sampling for faster rendering on large datasets
- Creates interactive marker clusters
- Exports the result as an HTML map

## Requirements

- Python 3.10 or later recommended
- pandas
- folium

Install dependencies:

```bash
pip install -r requirements.txt
```

## Input Data

The default input file is:

```text
data/koala_selected_columns.csv
```

Expected key columns:
- `Latitude`
- `Longitude`
- `ScientificName`
- `StartDate`
- `EndDate`
- `LocalityDetails`
- `ProjectName`
- `OrganisationAcronym`

## How to Run

```bash
python koala_map_generator.py
```

After execution, the generated map will be saved to:

```text
outputs/koala_map_emoji.html
```

## Main Workflow

1. Read the koala CSV dataset
2. Convert latitude and longitude to numeric values
3. Remove rows with invalid coordinates
4. Sample up to 5000 records for map performance
5. Create a Folium map centered on the sampled coordinates
6. Add clustered koala emoji markers
7. Save the final interactive map as HTML

## Customization

You can adjust these settings inside `koala_map_generator.py`:
- `INPUT_CSV`: input dataset path
- `OUTPUT_HTML`: output HTML path
- `SAMPLE_N`: number of plotted records
- `ZOOM_START`: initial zoom level

## Notes

- Rendering all records may be slow depending on dataset size.
- Sampling is enabled by default to keep the map responsive.
- This repository is structured for GitHub upload and reuse.

프로젝트 개요

이 프로젝트는 호주 전역의 코알라 위치 데이터를 지도 위에 시각화하는 파이썬 프로젝트임.

코알라 발생 위치 데이터(Occurrence Data)를 Pandas로 처리하고,
Folium 라이브러리를 사용하여 인터랙티브 지도 위에 시각화함.

파이썬을 이용한 지리 데이터 시각화(Geospatial Data Visualization)의
간단하고 직관적인 예제를 제공하는 것이 목적임.

주요 기능

코알라 위치 데이터 지도 시각화

Folium 기반 인터랙티브 지도 생성

Pandas를 이용한 데이터 처리

재현 가능한 간단한 파이썬 분석 코드

프로젝트 구조

koala-occurrence-map-australia
│
├─ data
│   └─ ko알라 위치 데이터(csv)
│
├─ outputs
│   └─ 생성된 지도(html)
│
├─ koala_map.py
├─ koala_map.ipynb
├─ requirements.txt
├─ README.md
├─ LICENSE
└─ .gitignore

설치 방법

필요한 라이브러리 설치

pip install -r requirements.txt

실행 방법

파이썬 코드 실행

python koala_map.py

실행 후 다음 파일이 생성됨

outputs/koala_map.html

해당 HTML 파일을 웹 브라우저에서 열면
코알라 위치가 표시된 인터랙티브 지도를 확인할 수 있음.

라이선스

이 프로젝트는 Apache License 2.0 라이선스를 따름.

작성자

YIRANG JUNG
## License

This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.

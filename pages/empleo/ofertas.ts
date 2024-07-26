// Para añadir una nueva oferta, crea una constante con la información correspondiente y añádela a la lista `ofertas` al final del archivo.

const beluck = {
    ocupación: 'NLP Engineer',
    "palabras clave": 'LLM, Pytorch, embeddings',
    contrato: 'T.Completo',
    entidad: 'beLuck',
    "nº trabajadores/as": '50-249',
    localización: 'Presencial en Asturias',
    "fecha publicación (fecha límite)": '2024/07/26 (2024/08/31)',
    más: 'https://www.beluck.es/trabajos/experto-a-en-programacion-de-lenguaje-natural-pln'
}

const all_jobs_bsc = {
    ocupación: 'Ofertas de investigación',
    "palabras clave": '',
    contrato: 'T.Completo',
    entidad: 'Barcelona Supercomputing Center (BSC)',
    "nº trabajadores/as": 'Más de 250',
    localización: 'Híbrido, Plaça Eusebi Güell, 1-3, 08034, Barcelona',
    "fecha publicación (fecha límite)": '2024/06/01 (2024/07/31)',
    más: 'https://www.bsc.es/join-us/job-opportunities'
}

const all_jobs_hitz = {
    ocupación: 'Ofertas de investigación',
    "palabras clave": '',
    contrato: 'T.Completo',
    entidad: 'Hitz Center for Language Technology, University of the Basque Country (UPV/EHU)',
    "nº trabajadores/as": 'Más de 250',
    localización: 'San Sebastian, Bilbao. Mínimo 30% presencial',
    "fecha publicación (fecha límite)": '2024/06/01',
    más: 'https://www.hitz.eus/job-offers'
}

const all_jobs_iic = {
    ocupación: 'Ofertas de empleo',
    "palabras clave": '',
    contrato: 'T.Completo',
    entidad: 'Instituto de Ingeniería del Conocimiento (IIC)',
    "nº trabajadores/as": 'Más de 250',
    localización: 'Campus de Cantoblanco de la UAM, Madrid',
    "fecha publicación (fecha límite)": '2024/06/01',
    más: 'https://www.iic.uam.es/empleo-iic/ofertas'
}


export const columnas = ['ocupación', 'contrato', 'entidad', 'nº trabajadores/as', 'localización', 'fecha publicación (fecha límite)', 'más']

export const ofertas = [
    beluck,
    all_jobs_bsc,
    all_jobs_hitz,
    all_jobs_iic
]

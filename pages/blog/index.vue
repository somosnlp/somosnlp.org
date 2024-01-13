<template>
    <Container class="my-12">
        <header class="m-auto text-center prose">
            <h1>Blog #NLP</h1>
            <a class="text-md" target="_blank" href="https://github.com/somosnlp/somosnlp.org/blob/main/CONTRIBUTING.md">
                ¿Qué quieres compartir con la comunidad?
            </a>
        </header>
        <hr class="mx-auto mt-8 mb-12 prose" />

        <div class="mx-auto mt-8 mb-12 prose italic">
            <ol>
                <li>
                    Crear un corpus de instrucciones de calidad que represente las variedades del español habladas por 600M
                    de personas, así como las lenguas cooficiales 💛
                </li>
                <li>
                    Estandarizar la evaluación de LLMs en estas ricas lenguas, permitiendo analizar el progreso y comparar
                    los modelos disponibles ✅
                </li>
                <li>
                    Ofreceros mayor soporte y visibilidad (¡porque estáis creando proyectos increíbles!) 🚀
                </li>
            </ol>

            <p>¿Quién se apunta? <a href="https://somosnlp.org/hackathon">somosnlp.org/hackathon</a></p>
        </div>
        <div class="mx-auto mt-8 mb-12 prose">
            <center>
                <a href="https://somosnlp.org/blog/nuestros-objetivos-para-2024" target="_blank"
                    style="background-color:#FACC15; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">¡Lee
                    más!</a>
            </center>
        </div>

        <hr class="mx-auto mt-8 mb-12 prose" />
        <BlogList />
        <hr class="mx-auto mt-8 mb-12 prose" />
        <footer class="m-auto text-center prose">
            <p>¿Te gustaría compartir algo con la comunidad?</p>
            <a class="text-md" target="_blank"
                href="https://github.com/somosnlp/somosnlp.org/blob/main/CONTRIBUTING.md#-publicar-un-art%C3%ADculo-en-el-blog">
                Publica en nuestro blog
            </a>
        </footer>
    </Container>
</template>

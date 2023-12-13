const Jimp = require('jimp');
const crypto = require('crypto');
const fs = require('fs');
const csv = require('csv-parser');

async function createDiploma(baseImagePath, name, project, prize) {
    const image = await Jimp.read(baseImagePath);
    const font = await Jimp.loadFont(Jimp.FONT_SANS_32_BLACK);

    image.print(font, 10, 10, `Name: ${name}`);
    image.print(font, 10, 50, `Project: ${project}`);
    image.print(font, 10, 90, `Prize: ${prize}`);

    return image;
}

function saveDiploma(image, name, project, prize) {
    const hash = crypto.createHash('sha256');
    hash.update(name + project + prize);
    const id = hash.digest('hex');

    image.write(`pages/certificados/${id}.png`);

    return id;
}

fs.createReadStream('pages/certificados/participantes.csv')
    .pipe(csv())
    .on('data', async (row) => {
        const image = await createDiploma('pages/certificados/dummy_diploma.jpeg', row.name, row.project, row.prize);
        const id = saveDiploma(image, row.name, row.project, row.prize);
        console.log(`Saved diploma with id ${id}`);
    });

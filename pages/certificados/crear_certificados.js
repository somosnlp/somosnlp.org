const Jimp = require('jimp'); // For image processing
const crypto = require('crypto'); // For generating unique hash
const fs = require('fs'); // For file system operations
const csv = require('csv-parser'); // For parsing CSV files

// Function to create a certificate
async function createCertificate(baseImagePath, name, project, prize) {
    const image = await Jimp.read(baseImagePath);
    const font = await Jimp.loadFont(Jimp.FONT_SANS_32_BLACK);

    // Define the text to print on the certificate
    const textName = `Name: ${name}`;
    const textProject = `Project: ${project}`;
    const textPrize = `Prize: ${prize}`;

    // Calculate the "x" position to center the text based on the image and text width
    const xName = (image.bitmap.width - Jimp.measureText(font, textName)) / 2;
    const xProject = (image.bitmap.width - Jimp.measureText(font, textProject)) / 2;
    const xPrize = (image.bitmap.width - Jimp.measureText(font, textPrize)) / 2;

    // Print the text
    image.print(font, xName, 10, textName);
    image.print(font, xProject, 50, textProject);
    image.print(font, xPrize, 90, textPrize);

    return image;
}

// Function to save the certificate image
function saveCertificate(image, name, project, prize) {
    // Create a SHA256 hash
    const hash = crypto.createHash('sha256');
    // Update the hash with the name, project, and prize
    hash.update(name + project + prize);
    // Get the hash value in hexadecimal format
    const id = hash.digest('hex');

    image.write(`pages/certificados/${id}.png`);
    return id;
}

// Read the CSV file containing participant data
fs.createReadStream('pages/certificados/participantes.csv')
    .pipe(csv()) // Parse the CSV data
    .on('data', async (row) => { // For each row in the CSV
        // Create a certificate
        const image = await createCertificate('pages/certificados/dummy_certificado.jpeg', row.name, row.project, row.prize);

        // Save the certificate image
        const id = saveCertificate(image, row.name, row.project, row.prize);

        // Log the saved certificate's ID
        console.log(`Saved certificate with ID ${id}`);
    });

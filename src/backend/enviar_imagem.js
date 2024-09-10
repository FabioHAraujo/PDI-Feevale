import fs from 'fs';
import FormData from 'form-data';
import fetch from 'node-fetch';

async function enviarImagem(caminhoDaImagem, nomeOriginal) {
    try {
        const formData = new FormData();
        formData.append('imagem', fs.createReadStream(caminhoDaImagem));
        formData.append('nome', nomeOriginal);

        const response = await fetch('https://pocket.fabioharaujo.com.br/api/collections/images_geradas/records', {
            method: 'POST',
            body: formData,
            headers: {
                ...formData.getHeaders()
            }
        });

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`HTTP error! status: ${response.status}, ${errorText}`);
        }

        const result = await response.json();

        // Construir a URL da imagem com base nos dados retornados
        const collectionId = result.collectionId;
        const imageFileName = result.imagem;  // Nome do arquivo
        const imageId = result.id;            // ID do arquivo
        const baseURL = 'https://pocket.fabioharaujo.com.br/api/files/';
        const imagemUrl = `${baseURL}${collectionId}/${imageId}/${imageFileName}?token=`;  // Ajuste o caminho conforme necessário

        // Retorne a URL como JSON
        console.log(JSON.stringify({ url: imagemUrl }));
    } catch (error) {
        console.error('Erro ao enviar a imagem:', error);
        process.exit(1);  // Sair com código de erro para indicar falha
    }
}

const caminhoDaImagem = process.argv[2];
const nomeOriginal = process.argv[3];
enviarImagem(caminhoDaImagem, nomeOriginal);

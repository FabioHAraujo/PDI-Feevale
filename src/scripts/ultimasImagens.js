import PocketBase from 'pocketbase';

const pb = new PocketBase('https://pocket.fabioharaujo.com.br');

async function obterUltimasImagens() {
    try {
        // Obtém as imagens com limite de 15, ordenadas pela data de criação
        const { items } = await pb.collection('images_geradas').getList(1, 15, {
            sort: '-created',
        });

        console.log(items);

        // Mapeie os registros para criar URLs completos para as imagens
        return items.map(record => {
            // Construa o URL completo da imagem
            return {
                id: record.id,
                imagem: pb.getFileUrl(record, record.imagem),
                nome: record.nome
            };
        });
    } catch (error) {
        console.error('Erro ao obter as últimas imagens:', error);
        return [];
    }
}

export default obterUltimasImagens;

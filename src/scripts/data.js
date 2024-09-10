import { ref } from 'vue';
import obterUltimasImagens from './ultimasImagens.js'; // Ajuste o caminho conforme necessário

// Refs para armazenar dados
export const imagens = ref([]);
export const quantidadeImagens = ref('0');
export const itens = ref([]);
export const imagemModal = ref(null); // Armazena a imagem a ser exibida no modal

export const responsiveOptions = ref([
    { breakpoint: '1500px', numVisible: 5 },
    { breakpoint: '1024px', numVisible: 3 },
    { breakpoint: '768px', numVisible: 2 },
    { breakpoint: '560px', numVisible: 1 }
]);

// Função para atualizar a quantidade de imagens e itens do menu
export async function atualizarUltimasImagens() {
    imagens.value = await obterUltimasImagens();

    // Atualize a quantidade de imagens no badge
    quantidadeImagens.value = imagens.value.length > 99 ? '+99' : imagens.value.length.toString();

    // Limpa o array de itens antes de adicionar novos elementos
    itens.value = [];

    // Adiciona as imagens ao menu
    for (let i = 0; i < imagens.value.length; i++) {
        itens.value.push({
            image: imagens.value[i].imagem,
            label: imagens.value[i].nome === '' ? 'teste.jpg' : imagens.value[i].nome
        });
    }
}

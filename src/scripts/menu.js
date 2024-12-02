import { ref, watchEffect } from 'vue';
import { quantidadeImagens, itens } from './data.js';
import { 
    abrirTransladarModal, 
    abrirRotacionarModal,
    abrirEspelharModal,
    abrirAumentarModal,
    abrirDiminuirModal,
    imagemAtual,
    desfazerUltimaOperacao,
    aplicarGrayscale,
    abrirGrayscaleModal,
    abrirLimiarModal,
    abrirMedianaModal,
    abrirGausianoModal,
    abrirSobelModal,
    abrirLaplaceModal,
    abrirDilatarModal,
    abrirErosaoModal,
    abrirAberturaModal,
    abrirFechamentoModal,
    abrirDominoModal
} from './functions.js';

// Definição do menu com o item "Últimas Imagens" usando a ref quantidadeImagens para o badge
export const items = ref([
    {
        label: 'Arquivo',
        icon: 'pi pi-file',
        items: [
            {
                label: 'Abrir',
                icon: 'pi pi-upload',
                shortcut: 'Ctrl+A'
            },
            {
                label: 'Salvar',
                icon: 'pi pi-save',
                shortcut: 'Ctrl+S'
            },
            {
                label: 'Sobre',
                icon: 'pi pi-info-circle',
                items: [
                    {
                        label: 'Os Devs',
                        icon: 'pi pi-code',
                    },
                    {
                        label: 'A Instituição',
                        icon: 'pi pi-compass',
                    }
                ]
            },
            {
                separator: true
            },
            {
                label: 'Sair',
                icon: 'pi pi-sign-out',
                shortcut: 'Ctrl+E'
            }
        ]
    },
    {
        label: 'Edição',
        icon: 'pi pi-hashtag',
        items: [
            {
                label: 'Transformações Geométricas',
                icon: 'pi pi-chevron-right',
                items: [
                    {
                        label: 'Transladar',
                        icon: 'pi pi-circle-on',
                        command: () => abrirTransladarModal()
                    },
                    {
                        label: 'Rotacionar',
                        icon: 'pi pi-circle-on',
                        command: () => abrirRotacionarModal()
                    },
                    {
                        label: 'Espelhar',
                        icon: 'pi pi-circle-on',
                        command: () => abrirEspelharModal()
                    },
                    {
                        label: 'Aumentar',
                        icon: 'pi pi-circle-on',
                        command: () => abrirAumentarModal()
                    },
                    {
                        label: 'Diminuir',
                        icon: 'pi pi-circle-on',
                        command: () => abrirDiminuirModal()
                    },
                ]
            },
            {
                label: 'Filtros',
                icon: 'pi pi-chevron-right',
                items: [
                    {
                        label: 'Grayscale',
                        icon: 'pi pi-circle-on',
                        command: () => abrirGrayscaleModal() // Chama a função aplicarGrayscale
                    },
                    {
                        label: 'Limiarização',
                        icon: 'pi pi-circle-on',
                        command: () => abrirLimiarModal() // Função que abre o modal para limiarização
                    },
                    {
                        label: 'Mediana',
                        icon: 'pi pi-circle-on',
                        command: () => abrirMedianaModal() // Função que abre o modal para aplicar o filtro mediano
                    },
                    {
                        label: 'Gausiano',
                        icon: 'pi pi-circle-on',
                        command: () => abrirGausianoModal() // Função que abre o modal para aplicar o filtro gaussiano
                    },
                    {
                        label: 'Sobel',
                        icon: 'pi pi-circle-on',
                        command: () => abrirSobelModal() // Função que abre o modal para aplicar o filtro sobel
                    },
                    {
                        label: 'Laplace (Extra)',
                        icon: 'pi pi-circle-on',
                        command: () => abrirLaplaceModal() // Função que abre o modal para aplicar o filtro laplaciano
                    },
                ]
            },
            {
                label: 'Morfologia Matemática',
                icon: 'pi pi-chevron-right',
                items: [
                    {
                        label: 'Dilatação',
                        icon: 'pi pi-circle-on',
                        command: () => abrirDilatarModal() // Função que abre o modal para aplicar Dilatação
                    },
                    {
                        label: 'Erosão',
                        icon: 'pi pi-circle-on',
                        command: () => abrirErosaoModal() // Função que abre o modal para aplicar Erosão
                    },
                    {
                        label: 'Abertura',
                        icon: 'pi pi-circle-on',
                        command: () => abrirAberturaModal() // Função que abre o modal para aplicar Abertura
                    },
                    {
                        label: 'Fechamento',
                        icon: 'pi pi-circle-on',
                        command: () => abrirFechamentoModal() // Função que abre o modal para aplicar Fechamento
                    },
                ]                
            },
            {
                label: 'Extração de Características',
                icon: 'pi pi-chevron-right',
                items: [
                    {
                        label: 'Contar Dominó',
                        icon: 'pi pi-star-fill',
                        command: () => abrirDominoModal()
                    },
                ]
            }
        ]
    },
    {
        label: 'Últimas Imagens',
        icon: 'pi pi-envelope',
        badge: quantidadeImagens, // Usando a ref quantidadeImagens para o badge
        items: itens.value.length > 0 ? itens.value : [], // Mostrar array vazio se não houver itens
        class: 'scrollable-dropdown' // Adiciona a classe para limitar o tamanho
    },
    {
        label: 'Desfazer',
        icon: 'pi pi-undo',
        command: () => desfazerUltimaOperacao()
    },
]);

watchEffect(() => {
    items.value[2].items = itens.value.length > 0 ? itens.value : [];
});

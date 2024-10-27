import { ref, watchEffect } from 'vue';
import { quantidadeImagens, itens } from './data.js';
import { 
    abrirTransladarModal, 
    abrirRotacionarModal,
    abrirEspelharModal,
    abrirAumentarModal,
    abrirDiminuirModal,
    imagemAtual,
    desfazerUltimaOperacao
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
                    },
                    {
                        label: 'Limiarização',
                        icon: 'pi pi-circle-on',
                    },
                    {
                        label: 'Mediana',
                        icon: 'pi pi-circle-on',
                    },
                    {
                        label: 'Gausiano',
                        icon: 'pi pi-circle-on',
                    },
                    {
                        label: 'Sobel',
                        icon: 'pi pi-circle-on',
                    },
                    {
                        label: 'Laplace (Extra)',
                        icon: 'pi pi-circle-on',
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
                    },
                    {
                        label: 'Erosão',
                        icon: 'pi pi-circle-on',
                    },
                    {
                        label: 'Abertura',
                        icon: 'pi pi-circle-on',
                    },
                    {
                        label: 'Fechamento',
                        icon: 'pi pi-circle-on',
                    },
                ]
            },
            {
                label: 'Extração de Características',
                icon: 'pi pi-chevron-right',
                items: [
                    {
                        label: 'Desafio',
                        icon: 'pi pi-star-fill',
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

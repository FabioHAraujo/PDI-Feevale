import { ref } from 'vue';
import axios from 'axios';

// Criação de uma variável reativa para controlar o modal
const imagemModal = ref(null);

// Função para abrir a imagem no modal
export function abrirImagem(item) {
    if (item) {
        imagemModal.value = item.items.image; // Use .value para atualizar o valor do ref
    } else {
        console.error('O item ou a propriedade image não está definido.');
    }
}

// Função para fechar o modal
export function fecharModal() {
    imagemModal.value = null;
}

// Função para formatar o tamanho do arquivo
export function formatSize(bytes) {
    if (bytes < 1024) return bytes + ' B';
    let kb = bytes / 1024;
    if (kb < 1024) return kb.toFixed(1) + ' KB';
    let mb = kb / 1024;
    return mb.toFixed(1) + ' MB';
}


// Função para remover um arquivo enviado
export function onRemoveUploadedFile(index, itens, quantidadeImagens) {
    const updatedItems = [...itens.value];
    updatedItems.splice(index, 1);
    itens.value = updatedItems;
    quantidadeImagens.value = itens.value.length > 99 ? '+99' : itens.value.length.toString();
}

// Controle do modal de translação
export const showTransladarModal = ref(false);
export const showRotacionarModal = ref(false);
export const showEspelharModal = ref(false);
export const showAumentarModal = ref(false);
export const showDiminuirModal = ref(false);

export const abrirTransladarModal = () => {
    showTransladarModal.value = true;
};

// Função para aplicar a translação
export const aplicarTranslacao = async (translacao, selectedImage) => {
    console.log('Translação:', translacao);
    console.log('Imagem selecionada:', selectedImage);

    if (translacao && typeof translacao.dx === 'number' && typeof translacao.dy === 'number' && selectedImage) {
        try {
            const formData = new FormData();
            formData.append('image', selectedImage);  // Usa o arquivo selecionado
            formData.append('operation', 'translacao');
            formData.append('params', `${translacao.dx},${translacao.dy}`);

            const response = await axios.post('https://pdi.fabioharaujo.com.br/processar_imagem/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            if (response.status === 200) {
                console.log('Imagem processada e enviada com sucesso!');
                const imagemUrl = response.data.url;  // Certifique-se de que este campo está no retorno da API
                return imagemUrl;
            } else {
                console.error('Falha ao processar a imagem:', response.data.message);
                return null;
            }
        } catch (error) {
            console.error('Erro ao enviar a requisição:', error);
            return null;
        } finally {
            showTransladarModal.value = false;  // Fecha o modal
        }
    } else {
        console.error("Translação ou imagem inválida.");
        return null;
    }
    
};

// Função para abrir o modal de rotação
export const abrirRotacionarModal = () => {
    showRotacionarModal.value = true;
};

// Função para aplicar a rotação
export const aplicarRotacao = async (angulo, selectedImage) => {
    console.log('Ângulo de rotação:', angulo);
    console.log('Imagem selecionada:', selectedImage);

    if (typeof angulo === 'number' && selectedImage) {
        try {
            const formData = new FormData();
            formData.append('image', selectedImage);
            formData.append('operation', 'rotacao');
            formData.append('params', angulo.toString());

            const response = await axios.post('https://pdi.fabioharaujo.com.br/processar_imagem/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            if (response.status === 200) {
                console.log('Imagem processada e enviada com sucesso!');
                const imagemUrl = response.data.url;
                return imagemUrl;
            } else {
                console.error('Falha ao processar a imagem:', response.data.message);
                return null;
            }
        } catch (error) {
            console.error('Erro ao enviar a requisição:', error);
            return null;
        } finally {
            showRotacionarModal.value = false;
        }
    } else {
        console.error("Ângulo ou imagem inválida.");
        return null;
    }
};

// Função para abrir o modal de espelhamento
export const abrirEspelharModal = () => {
    showEspelharModal.value = true;
};

// Função para aplicar o espelhamento
export const aplicarEspelhamento = async (eixo, selectedImage) => {
    console.log('Eixo de espelhamento:', eixo);
    console.log('Imagem selecionada:', selectedImage);

    if (eixo && selectedImage) {
        try {
            const formData = new FormData();
            formData.append('image', selectedImage);
            formData.append('operation', 'espelhamento');
            if(eixo==='horizontal'){
                eixo = 2
                formData.append('params', eixo);
            } else if(eixo==='vertical'){
                eixo = 1
                formData.append('params', eixo);
            }

            const response = await axios.post('https://pdi.fabioharaujo.com.br/processar_imagem/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            if (response.status === 200) {
                console.log('Imagem processada e enviada com sucesso!');
                const imagemUrl = response.data.url;
                return imagemUrl;
            } else {
                console.error('Falha ao processar a imagem:', response.data.message);
                return null;
            }
        } catch (error) {
            console.error('Erro ao enviar a requisição:', error);
            return null;
        } finally {
            showEspelharModal.value = false;
        }
    } else {
        console.error("Eixo ou imagem inválida.");
        return null;
    }
};

// Função para abrir o modal de aumento
export const abrirAumentarModal = () => {
    showAumentarModal.value = true;
};

// Função para aplicar o aumento
export const aplicarAumento = async (fator, selectedImage) => {
    console.log('Fator de aumento:', fator);
    console.log('Imagem selecionada:', selectedImage);

    if (typeof fator === 'number' && selectedImage) {
        try {
            const formData = new FormData();
            formData.append('image', selectedImage);
            formData.append('operation', 'escala');
            formData.append('params', fator.toString());

            const response = await axios.post('https://pdi.fabioharaujo.com.br/processar_imagem/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            if (response.status === 200) {
                console.log('Imagem processada e enviada com sucesso!');
                const imagemUrl = response.data.url;
                return imagemUrl;
            } else {
                console.error('Falha ao processar a imagem:', response.data.message);
                return null;
            }
        } catch (error) {
            console.error('Erro ao enviar a requisição:', error);
            return null;
        } finally {
            showAumentarModal.value = false;
        }
    } else {
        console.error("Fator ou imagem inválida.");
        return null;
    }
};

// Função para abrir o modal de diminuição
export const abrirDiminuirModal = () => {
    showDiminuirModal.value = true;
};

// Função para aplicar a diminuição
export const aplicarDiminuicao = async (fator, selectedImage) => {
    console.log('Fator de diminuição:', fator);
    console.log('Imagem selecionada:', selectedImage);

    // Converte o fator para um valor decimal entre 0 e 1
    const fatorDecimal = 1 / fator;
    console.log("Decimal: ", fatorDecimal)

    if (typeof fator === 'number' && selectedImage) {
        try {
            const formData = new FormData();
            formData.append('image', selectedImage);
            formData.append('operation', 'escala');
            formData.append('params', fatorDecimal.toString());

            const response = await axios.post('https://pdi.fabioharaujo.com.br/processar_imagem/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });

            if (response.status === 200) {
                console.log('Imagem processada e enviada com sucesso!');
                const imagemUrl = response.data.url;
                return imagemUrl;
            } else {
                console.error('Falha ao processar a imagem:', response.data.message);
                return null;
            }
        } catch (error) {
            console.error('Erro ao enviar a requisição:', error);
            return null;
        } finally {
            showDiminuirModal.value = false;
        }
    } else {
        console.error("Fator ou imagem inválida.");
        return null;
    }
};


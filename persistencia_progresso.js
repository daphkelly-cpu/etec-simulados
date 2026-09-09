/**
 * Módulo de Persistência de Progresso - ETEC Dashboard
 * Salva: respostas do simulado, histórico, progresso do plano, questões para revisar
 */

const ProgressoPersistencia = {
  
  // ===== SIMULADO ATUAL =====
  
  salvarRespostaSimulado(questaoId, alternativaSelecionada) {
    let simulado = this.obterSimuladoEmProgresso();
    if (!simulado.respostas) simulado.respostas = {};
    simulado.respostas[questaoId] = alternativaSelecionada;
    localStorage.setItem('simulado_em_progresso', JSON.stringify(simulado));
  },
  
  obterSimuladoEmProgresso() {
    const simulado = localStorage.getItem('simulado_em_progresso');
    return simulado ? JSON.parse(simulado) : {
      provaId: null,
      dataInicio: null,
      respostas: {},
      tempoRestante: 14400 // 4 horas em segundos
    };
  },
  
  iniciarSimulado(provaId) {
    const simulado = {
      provaId: provaId,
      dataInicio: new Date().toISOString(),
      respostas: {},
      tempoRestante: 14400
    };
    localStorage.setItem('simulado_em_progresso', JSON.stringify(simulado));
  },
  
  salvarTempoRestante(segundos) {
    let simulado = this.obterSimuladoEmProgresso();
    simulado.tempoRestante = segundos;
    localStorage.setItem('simulado_em_progresso', JSON.stringify(simulado));
  },
  
  // ===== HISTÓRICO DE SIMULADOS =====
  
  finalizarSimulado(provaId, gabarito, tempoGasto) {
    const simulado = this.obterSimuladoEmProgresso();
    
    // Calcular score
    let acertos = 0;
    Object.keys(simulado.respostas).forEach(questaoId => {
      if (simulado.respostas[questaoId] === gabarito[questaoId]) {
        acertos++;
      }
    });
    
    const scorePercentual = (acertos / Object.keys(simulado.respostas).length) * 100;
    
    // Criar registro no histórico
    const registro = {
      id: Date.now(),
      provaId: provaId,
      dataRealizacao: simulado.dataInicio,
      acertos: acertos,
      total: Object.keys(simulado.respostas).length,
      scorePercentual: scorePercentual.toFixed(1),
      tempoGasto: tempoGasto,
      respostas: simulado.respostas
    };
    
    // Adicionar ao histórico
    let historico = this.obterHistorico();
    historico.push(registro);
    localStorage.setItem('historico_simulados', JSON.stringify(historico));
    
    // Limpar simulado em progresso
    localStorage.removeItem('simulado_em_progresso');
    
    return registro;
  },
  
  obterHistorico() {
    const historico = localStorage.getItem('historico_simulados');
    return historico ? JSON.parse(historico) : [];
  },
  
  obterHistoricoPorProva(provaId) {
    return this.obterHistorico().filter(r => r.provaId === provaId);
  },
  
  // ===== PROGRESSO DO PLANO =====
  
  marcarSemanaCompleta(numeroSemana) {
    let progresso = this.obterProgressoPlano();
    if (!progresso.semanas) progresso.semanas = {};
    progresso.semanas[numeroSemana] = {
      completa: true,
      dataConclusa: new Date().toISOString()
    };
    localStorage.setItem('progresso_plano', JSON.stringify(progresso));
  },
  
  marcarTopicoCompleto(numeroSemana, topico) {
    let progresso = this.obterProgressoPlano();
    if (!progresso.topicos) progresso.topicos = {};
    const chave = `${numeroSemana}_${topico}`;
    progresso.topicos[chave] = {
      completo: true,
      dataConclusa: new Date().toISOString()
    };
    localStorage.setItem('progresso_plano', JSON.stringify(progresso));
  },
  
  obterProgressoPlano() {
    const progresso = localStorage.getItem('progresso_plano');
    return progresso ? JSON.parse(progresso) : {
      semanas: {},
      topicos: {}
    };
  },
  
  obterPercentualPlano() {
    const progresso = this.obterProgressoPlano();
    const semanasConcluidas = Object.keys(progresso.semanas).length;
    return (semanasConcluidas / 12) * 100;
  },
  
  // ===== QUESTÕES PARA REVISAR =====
  
  marcarParaRevisar(questaoId, prova) {
    let para_revisar = this.obterParaRevisar();
    const questao = {
      questaoId: questaoId,
      prova: prova,
      dataMarcada: new Date().toISOString(),
      revisada: false
    };
    para_revisar.push(questao);
    localStorage.setItem('questoes_para_revisar', JSON.stringify(para_revisar));
  },
  
  desmarcarParaRevisar(questaoId) {
    let para_revisar = this.obterParaRevisar();
    para_revisar = para_revisar.filter(q => q.questaoId !== questaoId);
    localStorage.setItem('questoes_para_revisar', JSON.stringify(para_revisar));
  },
  
  marcarComoRevisada(questaoId) {
    let para_revisar = this.obterParaRevisar();
    const questao = para_revisar.find(q => q.questaoId === questaoId);
    if (questao) {
      questao.revisada = true;
      questao.dataRevisada = new Date().toISOString();
      localStorage.setItem('questoes_para_revisar', JSON.stringify(para_revisar));
    }
  },
  
  obterParaRevisar() {
    const para_revisar = localStorage.getItem('questoes_para_revisar');
    return para_revisar ? JSON.parse(para_revisar) : [];
  },
  
  obterParaRevisarPendentes() {
    return this.obterParaRevisar().filter(q => !q.revisada);
  },
  
  // ===== EXPORTAR/IMPORTAR DADOS =====
  
  exportarTodosDados() {
    return {
      simulado_em_progresso: this.obterSimuladoEmProgresso(),
      historico_simulados: this.obterHistorico(),
      progresso_plano: this.obterProgressoPlano(),
      questoes_para_revisar: this.obterParaRevisar(),
      dataExportacao: new Date().toISOString()
    };
  },
  
  importarDados(dados) {
    if (dados.simulado_em_progresso) {
      localStorage.setItem('simulado_em_progresso', JSON.stringify(dados.simulado_em_progresso));
    }
    if (dados.historico_simulados) {
      localStorage.setItem('historico_simulados', JSON.stringify(dados.historico_simulados));
    }
    if (dados.progresso_plano) {
      localStorage.setItem('progresso_plano', JSON.stringify(dados.progresso_plano));
    }
    if (dados.questoes_para_revisar) {
      localStorage.setItem('questoes_para_revisar', JSON.stringify(dados.questoes_para_revisar));
    }
  },
  
  limparTodosDados() {
    localStorage.removeItem('simulado_em_progresso');
    localStorage.removeItem('historico_simulados');
    localStorage.removeItem('progresso_plano');
    localStorage.removeItem('questoes_para_revisar');
  },
  
  // ===== ESTATÍSTICAS =====
  
  obterEstatisticas() {
    const historico = this.obterHistorico();
    
    if (historico.length === 0) {
      return {
        simuladosRealizados: 0,
        mediaGeral: 0,
        acertosTotal: 0,
        questoesTotal: 0,
        melhorScore: 0,
        piorScore: 0
      };
    }
    
    const acertosTotal = historico.reduce((sum, r) => sum + r.acertos, 0);
    const questoesTotal = historico.reduce((sum, r) => sum + r.total, 0);
    const scores = historico.map(r => parseFloat(r.scorePercentual));
    
    return {
      simuladosRealizados: historico.length,
      mediaGeral: (scores.reduce((a, b) => a + b, 0) / scores.length).toFixed(1),
      acertosTotal: acertosTotal,
      questoesTotal: questoesTotal,
      melhorScore: Math.max(...scores),
      piorScore: Math.min(...scores)
    };
  }
};

// Exportar para uso global
if (typeof module !== 'undefined' && module.exports) {
  module.exports = ProgressoPersistencia;
}

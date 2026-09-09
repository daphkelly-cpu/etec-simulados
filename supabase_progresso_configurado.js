/**
 * Integração Supabase - Persistência de Progresso ETEC
 * CREDENCIAIS CONFIGURADAS ✅
 */

const SupabaseProgresso = {
  
  supabaseUrl: 'https://utsochxwjcklfbpjqfmk.supabase.co',
  supabaseKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV0c29jaHh3amNrbGZicGpxZm1rIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODg5MTA4OTMsImV4cCI6MjEwNDQ4Njg5M30.t1zMel5TtruFqpqGHoLCjoFSj9KnCPPMmUTKoQrvzCE',
  
  async inicializar() {
    console.log('✅ Supabase conectado:', this.supabaseUrl);
  },
  
  // ===== SIMULADOS =====
  
  async salvarSimulado(provaId, respostas, gabarito, tempoGasto) {
    try {
      let acertos = 0;
      Object.keys(respostas).forEach(questaoId => {
        if (respostas[questaoId] === gabarito[questaoId]) {
          acertos++;
        }
      });
      
      const scorePercentual = (acertos / Object.keys(respostas).length) * 100;
      
      const dados = {
        prova_id: provaId,
        data_realizacao: new Date().toISOString(),
        acertos: acertos,
        total: Object.keys(respostas).length,
        score_percentual: parseFloat(scorePercentual.toFixed(1)),
        tempo_gasto: tempoGasto,
        respostas: JSON.stringify(respostas)
      };
      
      const response = await fetch(`${this.supabaseUrl}/rest/v1/simulados`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.supabaseKey}`
        },
        body: JSON.stringify(dados)
      });
      
      if (!response.ok) throw new Error('Erro ao salvar simulado');
      console.log('✅ Simulado salvo no Supabase');
      return await response.json();
      
    } catch (error) {
      console.error('❌ Erro:', error);
    }
  },
  
  async obterTodosSimulados() {
    try {
      const response = await fetch(
        `${this.supabaseUrl}/rest/v1/simulados?order=data_realizacao.desc`,
        {
          headers: {
            'Authorization': `Bearer ${this.supabaseKey}`
          }
        }
      );
      
      if (!response.ok) throw new Error('Erro ao buscar simulados');
      return await response.json();
      
    } catch (error) {
      console.error('❌ Erro:', error);
      return [];
    }
  },
  
  // ===== PROGRESSO PLANO =====
  
  async marcarSemanaCompleta(numeroSemana) {
    try {
      const dados = {
        numero_semana: numeroSemana,
        completa: true,
        data_conclusao: new Date().toISOString()
      };
      
      const response = await fetch(`${this.supabaseUrl}/rest/v1/progresso_plano`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.supabaseKey}`
        },
        body: JSON.stringify(dados)
      });
      
      if (!response.ok) throw new Error('Erro ao marcar semana');
      console.log(`✅ Semana ${numeroSemana} marcada como completa`);
      return await response.json();
      
    } catch (error) {
      console.error('❌ Erro:', error);
    }
  },
  
  async obterProgressoPlano() {
    try {
      const response = await fetch(
        `${this.supabaseUrl}/rest/v1/progresso_plano?order=numero_semana.asc`,
        {
          headers: {
            'Authorization': `Bearer ${this.supabaseKey}`
          }
        }
      );
      
      if (!response.ok) throw new Error('Erro ao buscar progresso');
      return await response.json();
      
    } catch (error) {
      console.error('❌ Erro:', error);
      return [];
    }
  },
  
  // ===== QUESTÕES PARA REVISAR =====
  
  async marcarParaRevisar(questaoId, provaId) {
    try {
      const dados = {
        questao_id: questaoId,
        prova_id: provaId,
        data_marcada: new Date().toISOString(),
        revisada: false
      };
      
      const response = await fetch(`${this.supabaseUrl}/rest/v1/para_revisar`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.supabaseKey}`
        },
        body: JSON.stringify(dados)
      });
      
      if (!response.ok) throw new Error('Erro ao marcar para revisar');
      console.log('✅ Questão marcada para revisar');
      
    } catch (error) {
      console.error('❌ Erro:', error);
    }
  },
  
  async obterParaRevisar() {
    try {
      const response = await fetch(
        `${this.supabaseUrl}/rest/v1/para_revisar?revisada=eq.false`,
        {
          headers: {
            'Authorization': `Bearer ${this.supabaseKey}`
          }
        }
      );
      
      if (!response.ok) throw new Error('Erro ao buscar para revisar');
      return await response.json();
      
    } catch (error) {
      console.error('❌ Erro:', error);
      return [];
    }
  },
  
  // ===== ESTATÍSTICAS =====
  
  async obterEstatisticas() {
    try {
      const simulados = await this.obterTodosSimulados();
      
      if (simulados.length === 0) {
        return {
          simulados_realizados: 0,
          media_geral: 0,
          acertos_total: 0,
          questoes_total: 0,
          melhor_score: 0,
          pior_score: 0
        };
      }
      
      const acertosTotal = simulados.reduce((sum, s) => sum + s.acertos, 0);
      const questoesTotal = simulados.reduce((sum, s) => sum + s.total, 0);
      const scores = simulados.map(s => s.score_percentual);
      
      return {
        simulados_realizados: simulados.length,
        media_geral: (scores.reduce((a, b) => a + b, 0) / scores.length).toFixed(1),
        acertos_total: acertosTotal,
        questoes_total: questoesTotal,
        melhor_score: Math.max(...scores),
        pior_score: Math.min(...scores)
      };
      
    } catch (error) {
      console.error('❌ Erro:', error);
      return null;
    }
  }
};

// Inicializar ao carregar
SupabaseProgresso.inicializar();

// Exportar para uso global
if (typeof module !== 'undefined' && module.exports) {
  module.exports = SupabaseProgresso;
}

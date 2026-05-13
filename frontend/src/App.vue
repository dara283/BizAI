<template>
  <div class="layout">

    <aside class="sidebar">
      <div class="sidebar-brand">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/>
          <rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/>
        </svg>
        <span>BizAI</span>
      </div>
      <nav class="sidebar-nav">
        <router-link to="/" class="nav-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
          </svg>
          Analysis
        </router-link>
        <router-link to="/history" class="nav-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>
          </svg>
          History
        </router-link>
        <router-link to="/settings" class="nav-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="3"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M4.93 4.93a10 10 0 0 0 0 14.14"/>
          </svg>
          Settings
        </router-link>
      </nav>
      <div class="sidebar-footer">
        <div class="user-badge">
          <div class="avatar">A</div>
          <div class="user-info">
            <span class="user-name">Analyst</span>
            <span class="user-role">Pro Plan</span>
          </div>
        </div>
      </div>
    </aside>

    <main class="main">
      <header class="topbar">
        <div>
          <h1 class="page-title">{{ pageTitle }}</h1>
          <p class="page-subtitle">{{ pageSubtitle }}</p>
        </div>
      </header>
      <router-view />
    </main>

  </div>
</template>

<script>
export default {
  computed: {
    pageTitle() {
      const titles = { '/': 'Business Intelligence', '/history': 'Analysis History', '/settings': 'Settings' };
      return titles[this.$route.path] || 'Business Intelligence';
    },
    pageSubtitle() {
      const subs = {
        '/': 'Analyse reports and extract actionable insights using AI',
        '/history': 'Review and revisit your previous analyses',
        '/settings': 'Configure your backend connection and preferences'
      };
      return subs[this.$route.path] || '';
    }
  }
};
</script>

<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Inter', sans-serif;
  background: #0a0f1e;
  color: #e2e8f0;
}

.layout {
  display: flex;
  min-height: 100vh;
}

/* ── Sidebar ── */
.sidebar {
  width: 220px;
  background: #0d1424;
  border-right: 1px solid #1e2d45;
  display: flex;
  flex-direction: column;
  padding: 24px 16px;
  flex-shrink: 0;
}

.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 17px;
  font-weight: 700;
  color: #f1f5f9;
  padding: 0 8px 28px;
  letter-spacing: 0.3px;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 4px;
  flex: 1;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 12px;
  border-radius: 8px;
  font-size: 13.5px;
  font-weight: 500;
  color: #64748b;
  cursor: pointer;
  transition: all 0.15s;
  text-decoration: none;
}

.nav-item:hover { background: #1e2d45; color: #cbd5e1; }
.nav-item.router-link-active { background: #1e3a5f; color: #60a5fa; }

.sidebar-footer { padding-top: 20px; border-top: 1px solid #1e2d45; }

.user-badge {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: #1e3a5f;
  color: #60a5fa;
  font-size: 13px;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
}

.user-info { display: flex; flex-direction: column; }
.user-name { font-size: 13px; font-weight: 600; color: #e2e8f0; }
.user-role { font-size: 11px; color: #475569; }

/* ── Main ── */
.main {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

.topbar {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 32px 40px 24px;
  border-bottom: 1px solid #1e2d45;
}

.page-title {
  font-size: 22px;
  font-weight: 700;
  color: #f1f5f9;
  letter-spacing: -0.3px;
}

.page-subtitle {
  font-size: 13.5px;
  color: #475569;
  margin-top: 4px;
}

/* ── Shared content layout ── */
.content {
  padding: 32px 40px;
  display: flex;
  flex-direction: column;
  gap: 28px;
}

.page-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.view-title {
  font-size: 18px;
  font-weight: 700;
  color: #f1f5f9;
}

.view-subtitle {
  font-size: 13px;
  color: #475569;
  margin-top: 4px;
}

/* ── Input Section ── */
.input-section {
  background: #0d1424;
  border: 1px solid #1e2d45;
  border-radius: 12px;
  padding: 24px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.section-label {
  font-size: 13px;
  font-weight: 600;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.6px;
}

.char-count { font-size: 12px; color: #334155; }

textarea {
  width: 100%;
  height: 160px;
  background: #0a0f1e;
  border: 1px solid #1e2d45;
  border-radius: 8px;
  color: #e2e8f0;
  font-family: 'Inter', sans-serif;
  font-size: 14px;
  line-height: 1.6;
  padding: 14px 16px;
  resize: vertical;
  outline: none;
  transition: border-color 0.2s;
}

textarea:focus { border-color: #3b82f6; }
textarea::placeholder { color: #334155; }
textarea:disabled { opacity: 0.5; cursor: not-allowed; }

.input-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 14px;
}

/* ── Buttons ── */
.btn-clear {
  padding: 9px 20px;
  border-radius: 7px;
  border: 1px solid #1e2d45;
  background: transparent;
  color: #64748b;
  font-family: 'Inter', sans-serif;
  font-size: 13.5px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s;
}

.btn-clear:hover:not(:disabled) { background: #1e2d45; color: #94a3b8; }
.btn-clear:disabled { opacity: 0.4; cursor: not-allowed; }

.btn-analyse {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 9px 24px;
  border-radius: 7px;
  border: none;
  background: #2563eb;
  color: #fff;
  font-family: 'Inter', sans-serif;
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.15s;
}

.btn-analyse:hover:not(:disabled) { background: #1d4ed8; }
.btn-analyse:disabled { opacity: 0.5; cursor: not-allowed; }

.btn-secondary {
  padding: 8px 18px;
  border-radius: 7px;
  border: 1px solid #1e2d45;
  background: transparent;
  color: #94a3b8;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s;
}

.btn-secondary:hover:not(:disabled) { background: #1e2d45; }
.btn-secondary:disabled { opacity: 0.4; cursor: not-allowed; }

.btn-danger {
  padding: 8px 18px;
  border-radius: 7px;
  border: 1px solid #7f1d1d;
  background: transparent;
  color: #fca5a5;
  font-family: 'Inter', sans-serif;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s;
}

.btn-danger:hover { background: #1c0a0a; }

.btn-icon {
  width: 30px;
  height: 30px;
  border-radius: 6px;
  border: 1px solid #1e2d45;
  background: transparent;
  color: #64748b;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s;
}

.btn-icon:hover { background: #1e2d45; color: #94a3b8; }
.btn-icon.danger:hover { background: #1c0a0a; color: #fca5a5; border-color: #7f1d1d; }

.spinner {
  width: 14px;
  height: 14px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top-color: #fff;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

/* ── Error ── */
.error-banner {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #1c0a0a;
  border: 1px solid #7f1d1d;
  color: #fca5a5;
  font-size: 13.5px;
  padding: 12px 16px;
  border-radius: 8px;
}

/* ── Results ── */
.results-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.result-card {
  background: #0d1424;
  border: 1px solid #1e2d45;
  border-radius: 12px;
  padding: 22px;
}

.result-card.full-width { grid-column: 1 / -1; }

.result-card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 12.5px;
  font-weight: 600;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  margin-bottom: 14px;
}

.result-icon {
  width: 28px;
  height: 28px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.summary-icon  { background: #1e3a5f; color: #60a5fa; }
.insights-icon { background: #1a2e1a; color: #4ade80; }
.reco-icon     { background: #2d1f3d; color: #a78bfa; }

.result-card p {
  font-size: 14px;
  line-height: 1.75;
  color: #94a3b8;
}

/* ── History ── */
.history-list { display: flex; flex-direction: column; gap: 12px; }

.history-card {
  background: #0d1424;
  border: 1px solid #1e2d45;
  border-radius: 12px;
  padding: 18px 22px;
}

.history-card-top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
}

.history-meta { flex: 1; }

.history-date {
  font-size: 11.5px;
  color: #475569;
  font-weight: 500;
  display: block;
  margin-bottom: 5px;
}

.history-preview {
  font-size: 13.5px;
  color: #64748b;
  line-height: 1.5;
}

.history-actions { display: flex; gap: 6px; flex-shrink: 0; }

.history-results { margin-top: 20px; }

/* ── Empty state ── */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  padding: 60px 20px;
  color: #334155;
  text-align: center;
  font-size: 14px;
}

/* ── Settings ── */
.settings-grid {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.settings-card {
  background: #0d1424;
  border: 1px solid #1e2d45;
  border-radius: 12px;
  padding: 24px;
}

.settings-section-title {
  font-size: 13px;
  font-weight: 600;
  color: #94a3b8;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  margin-bottom: 20px;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 7px;
  margin-bottom: 18px;
}

.field:last-child { margin-bottom: 0; }

.field label {
  font-size: 13px;
  font-weight: 500;
  color: #cbd5e1;
}

.field input, .field select {
  background: #0a0f1e;
  border: 1px solid #1e2d45;
  border-radius: 7px;
  color: #e2e8f0;
  font-family: 'Inter', sans-serif;
  font-size: 13.5px;
  padding: 9px 13px;
  outline: none;
  transition: border-color 0.2s;
}

.field input:focus, .field select:focus { border-color: #3b82f6; }
.field select option { background: #0d1424; }

.field-hint { font-size: 12px; color: #475569; }

.connection-row { display: flex; align-items: center; gap: 12px; }

.status-pill {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12.5px;
  font-weight: 500;
  color: #475569;
  background: #0a0f1e;
  border: 1px solid #1e2d45;
  padding: 5px 12px;
  border-radius: 20px;
}

.status-pill .dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #475569;
}

.status-pill.ok { color: #34d399; border-color: #064e3b; }
.status-pill.ok .dot { background: #34d399; }
.status-pill.fail { color: #fca5a5; border-color: #7f1d1d; }
.status-pill.fail .dot { background: #fca5a5; }

.settings-footer {
  display: flex;
  align-items: center;
  gap: 16px;
}

.saved-label {
  font-size: 13px;
  color: #34d399;
}

/* ── Transition ── */
.fade-enter-active { transition: opacity 0.35s ease, transform 0.35s ease; }
.fade-enter-from   { opacity: 0; transform: translateY(10px); }
</style>

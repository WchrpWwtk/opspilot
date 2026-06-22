const backendHealthUrl = "http://127.0.0.1:8000/health";

export default function Home() {
  return (
    <main className="page-shell">
      <section className="hero" aria-labelledby="project-title">
        <div className="hero-content">
          <p className="eyebrow">Current milestone</p>
          <h1 id="project-title">OpsPilot AI</h1>
          <p className="description">
            A production-style internal operations workflow platform for practicing full stack
            engineering, auditability, and future AI-assisted workflows.
          </p>

          <dl className="status-list" aria-label="Project status">
            <div className="status-item">
              <dt>Milestone</dt>
              <dd>M1C Frontend Shell</dd>
            </div>
            <div className="status-item">
              <dt>Backend health check</dt>
              <dd>
                <code>{backendHealthUrl}</code>
              </dd>
            </div>
          </dl>
        </div>
      </section>
    </main>
  );
}

function Header() {
  return (
    <header className="header">

      <div className="brand">

        <div className="brand-logo">
          AI
        </div>

        <div>
          <h1>AIVOA</h1>
          <span>AI Complaint Management</span>
        </div>

      </div>

      <div className="header-right">
        <span className="system-status">
          <span className="status-dot"></span>
          AI System Online
        </span>
      </div>

    </header>
  );
}

export default Header;
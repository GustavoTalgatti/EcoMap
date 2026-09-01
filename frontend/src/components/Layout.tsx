import { Link, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import styles from "./Layout.module.css";

export default function Layout() {
  const { user, logout } = useAuth();

  return (
    <div className={styles.layout}>
      <header className={styles.header}>
        <Link to="/" className={styles.logo}>
          EcoMap
        </Link>
        <nav className={styles.nav}>
          <Link to="/" className={styles.navLink}>
            Mapa
          </Link>
          <Link to="/guia" className={styles.navLink}>
            Guia
          </Link>
          <Link to="/sugerir" className={styles.navLink}>
            Sugerir Ponto
          </Link>
          {user ? (
            <>
              <span className={styles.userName}>Olá, {user.name}</span>
              <button type="button" className={styles.logoutBtn} onClick={logout}>
                Sair
              </button>
            </>
          ) : (
            <>
              <Link to="/login" className={styles.navLink}>
                Entrar
              </Link>
              <Link to="/register" className={styles.navLink}>
                Cadastrar
              </Link>
            </>
          )}
        </nav>
      </header>
      <main className={styles.main}>
        <Outlet />
      </main>
    </div>
  );
}

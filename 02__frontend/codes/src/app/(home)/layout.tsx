'use client'
import './home.css';
import "primereact/resources/themes/bootstrap4-dark-purple/theme.css";
import "primereact/resources/primereact.min.css";
import 'primeicons/primeicons.css';
import { Menu } from 'primereact/menu';

export default function RootLayout({
    children
}: {
    children: React.ReactNode
}) {
    const items = [
        { label: 'Livros', url: '/books', icon: 'pi pi-fw pi-book' },
        { label: 'Autores', url: '/authors', icon: 'pi pi-fw pi-user' },
        { label: 'Assuntos', url: '/subjects', icon: 'pi pi-fw pi-comment' },
        { label: 'Sair', url: '/login', icon: 'pi pi-fw pi-sign-out' },
    ]
    return (
        <main className='main_home'>
            <Menu model={items} style={{ 'minHeight': '100vh', 'minWidth': '12rem' }} />
            <div className="container">
                {children}
            </div>
        </main>
    )
}

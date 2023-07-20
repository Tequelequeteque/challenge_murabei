'use client'
import { useEffect } from 'react';
import './login.css'
import { useRouter } from 'next/navigation'
import Api from '@/utils/api'

export default function Login() {    
    const router = useRouter();
    useEffect(() => {
        localStorage.removeItem('library_token')
        return () => { }
    }, []);

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault()
        const data = await Api.post<{token:string}>('/auth', {
            user: event.currentTarget.user.value,
            password: event.currentTarget.password.value
        }).catch((e) => {
                console.error(e)
                return null;
        })
        if (data) {
            localStorage.setItem('library_token', data.token)
            router.push('/books')
        }
    }

    return (
        <main className='main_login'>
            <form onSubmit={handleSubmit} className='form_login'>
                <h1>Username</h1>
                <input type='text' name='user' />
                <h1>Password</h1>
                <input type='password' name='password' />
                <div className='container'>
                    <button type='submit'>Login</button>
                    <button>Cancel</button>
                </div>
            </form>
        </main>
    )
}
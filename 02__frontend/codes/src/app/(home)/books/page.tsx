'use client'

import './books.css'
import { useRouter } from 'next/navigation'
import { useCallback, useEffect, useRef, useState } from 'react'
import { DataTable } from 'primereact/datatable';
import { Panel } from 'primereact/panel';
import { Column } from 'primereact/column';
import { Button } from 'primereact/button';
import Api from '@/utils/api';
import { Toast } from 'primereact/toast';

export default function BookPage()  {
    const toast = useRef<Toast>(null)
    const router = useRouter()
    const [page, setPage] = useState(1)

    const [books, setBooks] = useState([] as any[])
    const getBooks = useCallback(
        () => {
            const token = localStorage.getItem('library_token')
            Api.get<any[]>('/books', {
                params: {
                    page: page
                },
            }).then(data => {
                if (data.length > 0) {
                    setBooks(data)
                }
            }).catch((e) => {
                router.push('/login')
            })
        },
        [page,router]
    )
    useEffect(() => {
        getBooks()
    }, [getBooks])

    const footer = () => {
        return <div className='container-footer'>
            <Button icon="pi pi-angle-left" className='flex' disabled={page == 1} onClick={() => setPage(Math.max(1, page - 1))} />
            <Button className='flex' label='Criar' onClick={() => router.push('/books/create')} />
            <Button icon="pi pi-angle-right" className='flex' onClick={() => setPage(page + 1)} />
        </div>
    }

    const deleteBookAction = useCallback((book: any) => {
        Api.delete('/books/' + book.id)
        .then((d) => {
            toast.current?.show({ severity: 'success', summary: 'Sucesso', detail: 'Livro deletado com sucesso', life: 3000 })
            getBooks()
        }).catch((e) => {
            console.error(e)
            toast.current?.show({ severity: 'error', summary: 'Erro', detail: 'Não foi possível deletar o livro', life: 3000 })
        })
    }, [getBooks])

    const actions = (book: any) => {
        return <div className='container-actions'>
            <Button icon="pi pi-pencil" className='flex' onClick={(e) => router.push(`/books/${book.id}`)} />
            <Button icon="pi pi-trash" severity="danger" className='flex' onClick={() => deleteBookAction(book)} />
        </div>
    }
    if(!books.length){
        return <i className="pi pi-spin pi-cog" style={{ fontSize: '2rem' }}></i>
    }
    return (
        <Panel header="Livros">
            <Toast ref={toast}></Toast>
            <DataTable
                value={books}
                lazy={true}
                size={'small'}
                footer={footer}
            >
                <Column field="title" header="Titulo" />
                <Column field="author" header="Autor" />
                <Column field="price" header="Preço" />
                <Column field="publisher" header="Editora" />
                <Column header="Ações" body={actions} />
            </DataTable>
        </Panel>
    )
}

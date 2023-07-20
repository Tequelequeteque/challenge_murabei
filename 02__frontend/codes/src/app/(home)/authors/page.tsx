'use client'

import './author.css'
import { useRouter } from 'next/navigation'
import { useCallback, useEffect, useState } from 'react'
import { DataTable } from 'primereact/datatable';
import { Panel } from 'primereact/panel';
import { Column } from 'primereact/column';
import { Button } from 'primereact/button';
import Api from '@/utils/api';

export default function AuthorPage() {
    const router = useRouter()
    const [page, setPage] = useState(1)

    const [authors, setAuthors] = useState([] as any[])
    const getAuthors = useCallback(
        () => {
            const token = localStorage.getItem('library_token')
            Api.get<any[]>('/authors', {
                params: {
                    page: page
                },
            }).then(data => {
                if (data.length > 0) {
                    setAuthors(data)
                }
            }).catch((e) => {
                router.push('/login')
            })
        },
        [page,router]
    )
    useEffect(() => {
        getAuthors()
    }, [getAuthors])

    const footer = () => {
        return <div className='container-footer'>
            <Button icon="pi pi-angle-left" className='flex' disabled={page == 1} onClick={() => setPage(Math.max(1, page - 1))} />
            <Button icon="pi pi-angle-right" className='flex' onClick={() => setPage(page + 1)} />
        </div>
    }

    if(!authors.length){
        return <i className="pi pi-spin pi-cog" style={{ fontSize: '2rem' }}></i>
    }

    return (
        <Panel header="Autores">
            <DataTable
                value={authors}
                lazy={true}
                size={'small'}
                footer={footer}
            >
                <Column field="title" header="Titulo" />
                <Column field="biography" header="Bibliografia" />
            </DataTable>
        </Panel>
    )
}

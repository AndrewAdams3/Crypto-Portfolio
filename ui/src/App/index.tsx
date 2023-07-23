import { useState, useEffect } from "react";
import { PortfolioBuilder } from "../PortfolioBuilder";
import * as classes from './app.module.css';

const userId = 2;
export function App() {
    const [portfolios, setPortfolios] = useState<any[]>([]);
    const [hasPortfolio, setHasPortfolio] = useState<boolean>(false);
    useEffect(() => {
        fetchPortfolios();
    }, [])
    
    const fetchPortfolios = async () => {
        const res = await fetch(`http://localhost:8000/portfolio/${userId}/`)
        const json = await res.json();
        setPortfolios(json);
        if(json.length > 0) {
            setHasPortfolio(true)
        }
    }

    const createPortfolio = () => {
        setPortfolios([...portfolios, { currencies: [], portfolio: {} }])
    }

    return (
        <div className={classes.app_container}>
            {
                portfolios.length > 0 ? portfolios.map((p) => (
                    <PortfolioBuilder key={p.id} portfolio={p} userId={userId} onCreatePortfolio={fetchPortfolios} hasPortfolio={hasPortfolio}/>
                )) :
                <div>
                    <button onClick={createPortfolio}>Create Portfolio</button>
                </div>
            }
        </div>
    );
}
import * as classes from './styles.module.css';

type CurrencyTileProps = {
    name: string;
    click: () => void;
    buttonText: string;
    marketCap?: string;
}

export function CurrencyTile({name, buttonText, click, marketCap}: CurrencyTileProps) {
    return (
        <div className={classes.currency_tile}>
            <p>{name}</p>
            { marketCap && <p>{marketCap}</p> }
            <button onClick={click}>{buttonText}</button>
        </div>
    );
}
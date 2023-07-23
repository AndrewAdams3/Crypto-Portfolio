import * as classes from './styles.module.css';

type CurrencyTileProps = {
    name: string;
    click: () => void;
    buttonText: string;
}

export function CurrencyTile({name, buttonText, click}: CurrencyTileProps) {
    return (
        <div className={classes.currency_tile}>
            <p>{name}</p>
            <button onClick={click}>{buttonText}</button>
        </div>
    );
}
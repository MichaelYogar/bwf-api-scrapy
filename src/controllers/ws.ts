import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import db from '../config/db';
import { queryWS } from '../db/queries';

const NAMESPACE = 'WS';

const getWS = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'WS');

    db.execute(queryWS).spread(function (players: string) {
        res.json(players);
    });
};

export default getWS;

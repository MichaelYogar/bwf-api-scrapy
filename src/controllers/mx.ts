import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import db from '../config/db';
import { queryMX } from '../db/queries';

const NAMESPACE = 'MX';

const getMX = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'MX');

    db.execute(queryMX).spread(function (players: string) {
        res.json(players);
    });
};

export default getMX;

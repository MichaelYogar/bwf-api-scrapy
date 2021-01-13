import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import db from '../config/db';
import { queryMS } from '../db/queries';

const NAMESPACE = 'MS';

const getMS = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'MS');

    db.execute(queryMS).spread(function (players: string) {
        res.json(players);
    });
};

export default getMS;

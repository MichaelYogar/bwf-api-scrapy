import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import db from '../config/db';
import { queryWD } from '../db/queries';

const NAMESPACE = 'WD';

const getWD = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'WD');

    db.execute(queryWD).spread(function (users: any) {
        res.json(users);
    });
};

export default getWD;

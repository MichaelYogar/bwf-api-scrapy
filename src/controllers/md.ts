import { NextFunction, Request, Response } from 'express';
import logging from '../config/logging';
import db from '../config/db';
import { queryMD } from '../db/queries';

const NAMESPACE = 'MD';

const getMD = async (req: Request, res: Response, next: NextFunction) => {
    logging.info(NAMESPACE, 'MD');

    db.execute(queryMD).spread(function (users: any) {
        res.json(users);
    });
};

export default getMD;

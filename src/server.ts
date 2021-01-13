import http from 'http';
import bodyParser from 'body-parser';
import express from 'express';
import cors from 'cors';
import logging from './config/logging';
import config from './config/config';
import routes from './routes';

const NAMESPACE = 'Server';
const router = express();

/** Log the request */
router.use((req, res, next) => {
    /** Log the req */
    logging.info(`METHOD: [${req.method}] - URL: [${req.url}] - IP: [${req.socket.remoteAddress}]`, NAMESPACE);

    res.on('finish', () => {
        /** Log the res */
        logging.info(`METHOD: [${req.method}] - URL: [${req.url}] - STATUS: [${res.statusCode}] - IP: [${req.socket.remoteAddress}]`, NAMESPACE);
    });

    next();
});

/** Parse the body of the request */
router.use(bodyParser.urlencoded({ extended: false })); // might need to set to true
router.use(bodyParser.json());

router.use(cors());

/** Routes */
router.use(routes);

/** Error handling */
router.use((req, res, next) => {
    const error = new Error('Not found');

    res.status(404).json({
        message: error.message
    });
});

const httpServer = http.createServer(router);

httpServer.listen(config.server.port, () => logging.info(NAMESPACE, `Server is running ${config.server.hostname}:${config.server.port}`));

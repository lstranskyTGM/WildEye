'use strict';

/**
 * camera controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::camera.camera');

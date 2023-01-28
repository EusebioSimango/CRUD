import fastify, { FastifyInstance, FastifyReply, FastifyRequest } from 'fastify'

const server = fastify()


server.get('/', async (request: FastifyRequest, reply: FastifyReply) => {
	return 'Hello, World!\n'
	// return { greet: 'hello, world!' }
})

server.listen({ port: 3333 }, (err: any, address: string) => {
	if (err) {
		console.error(err)
		process.exit(1)
	}
	console.log(`Server listening at ${address}`)
})
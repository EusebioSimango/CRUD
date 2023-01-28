import fastify, { FastifyInstance, FastifyReply, FastifyRequest } from 'fastify'
import { z } from 'zod'

const userSchema = z.object({
	name: z.string().min(3, { message: 'Name must have more than 3 chars.' }),
	age: z.number().min(15, { message: 'You must be 15 years or older.'})
})

type User = z.infer<typeof userSchema>

const server = fastify({ logger: true })

server.get('/', async (request: FastifyRequest, reply: FastifyReply) => {
	const eusebio: User = userSchema.parse({ name: 'Eusébio', age: 15 })
	return { user: eusebio }
})

server.listen({ port: 3333 }, (err: any, address: string) => {
	if (err) {
		server.log.error(err)
		process.exit(1)
	}
	server.log.info(`Server listening at ${address}`)
})